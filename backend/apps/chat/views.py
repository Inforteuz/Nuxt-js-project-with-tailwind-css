import json
import logging
import urllib.request
import urllib.error

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny

from .models import AIConfig, KnowledgeItem

logger = logging.getLogger(__name__)

MAX_HISTORY = 10   # keep last N user/assistant turns


def _build_knowledge_block():
    """Return a formatted string of all active knowledge items."""
    items = KnowledgeItem.objects.filter(is_active=True).order_by('category', 'order')
    if not items.exists():
        return ""
    lines = ["\n\n## Bilimlar bazasi (quyidagi ma'lumotlar asosida javob bering):\n"]
    current_cat = None
    for item in items:
        if item.category != current_cat:
            current_cat = item.category
            lines.append(f"\n### {item.get_category_display()}\n")
        lines.append(f"**{item.title}**\n{item.content}\n")
    return "".join(lines)


def _call_openai_compatible(api_key, base_url, model, messages, temperature, max_tokens):
    """Call any OpenAI-compatible API (OpenAI, OpenRouter, Groq)."""
    payload = json.dumps({
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }).encode("utf-8")

    req = urllib.request.Request(
        f"{base_url}/chat/completions",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


def _call_gemini(api_key, model, messages, temperature, max_tokens):
    """Call Google Gemini REST API."""
    # Convert OpenAI-style messages → Gemini format
    contents = []
    for msg in messages:
        role = "user" if msg["role"] == "user" else "model"
        if msg["role"] == "system":
            # Gemini has no system role; prepend to first user turn
            continue
        contents.append({"role": role, "parts": [{"text": msg["content"]}]})

    # Extract system instruction
    sys_text = next((m["content"] for m in messages if m["role"] == "system"), "")

    payload = json.dumps({
        "system_instruction": {"parts": [{"text": sys_text}]} if sys_text else None,
        "contents": contents,
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": max_tokens,
        },
    }).encode("utf-8")

    # Remove None values from payload
    data_dict = json.loads(payload)
    if data_dict.get("system_instruction") is None:
        del data_dict["system_instruction"]

    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}",
        data=json.dumps(data_dict).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["candidates"][0]["content"]["parts"][0]["text"]


class ChatConfigView(APIView):
    """Return public chat config (welcome message, is_active). No API key exposed."""
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request):
        cfg = AIConfig.objects.filter(is_active=True).first()
        if not cfg:
            return Response({"is_active": False})
        return Response({
            "is_active": True,
            "welcome_uz": cfg.welcome_message_uz,
            "welcome_ru": cfg.welcome_message_ru,
            "welcome_kr": cfg.welcome_message_kr,
        })


class ChatView(APIView):
    """
    POST /api/v1/chat/
    Body: { "message": "...", "history": [{"role": "user"|"assistant", "content": "..."}] }
    Response: { "reply": "..." }
    """
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        user_message = (request.data.get("message") or "").strip()
        if not user_message:
            return Response({"error": "Xabar bo'sh bo'lishi mumkin emas."}, status=400)

        cfg = AIConfig.objects.filter(is_active=True).first()
        if not cfg:
            return Response({"error": "AI yordamchi hozircha faol emas."}, status=503)

        # Build full system prompt with knowledge base
        system_content = cfg.system_prompt + _build_knowledge_block()

        # Build message list
        history = request.data.get("history", [])
        # Sanitize history: keep only last MAX_HISTORY turns, valid roles only
        safe_history = [
            {"role": h["role"], "content": str(h["content"])[:2000]}
            for h in history[-MAX_HISTORY:]
            if h.get("role") in ("user", "assistant") and h.get("content")
        ]

        messages = [{"role": "system", "content": system_content}] + safe_history + [
            {"role": "user", "content": user_message}
        ]

        try:
            reply = self._dispatch(cfg, messages)
            return Response({"reply": reply})
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")
            logger.error("AI API HTTPError %s: %s", e.code, body)
            return Response(
                {"error": f"AI xizmatida xatolik ({e.code}). Keyinroq urinib ko'ring."},
                status=502,
            )
        except Exception as exc:
            logger.exception("AI chat error: %s", exc)
            return Response(
                {"error": "AI xizmatiga ulanishda xatolik yuz berdi."},
                status=502,
            )

    def _dispatch(self, cfg, messages):
        p = cfg.provider
        if p == "gemini":
            return _call_gemini(
                cfg.api_key, cfg.model_name,
                messages, cfg.temperature, cfg.max_tokens,
            )
        elif p == "openai":
            return _call_openai_compatible(
                cfg.api_key,
                "https://api.openai.com/v1",
                cfg.model_name, messages,
                cfg.temperature, cfg.max_tokens,
            )
        elif p == "openrouter":
            return _call_openai_compatible(
                cfg.api_key,
                "https://openrouter.ai/api/v1",
                cfg.model_name, messages,
                cfg.temperature, cfg.max_tokens,
            )
        elif p == "groq":
            return _call_openai_compatible(
                cfg.api_key,
                "https://api.groq.com/openai/v1",
                cfg.model_name, messages,
                cfg.temperature, cfg.max_tokens,
            )
        else:
            raise ValueError(f"Noma'lum provayder: {p}")
