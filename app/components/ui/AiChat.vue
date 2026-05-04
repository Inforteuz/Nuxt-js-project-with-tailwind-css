<template>
  <!-- Always show the widget; chat sends friendly message if not configured -->
  <div class="ai-chat-widget">

    <!-- Floating toggle button -->
    <button
      @click="toggleChat"
      :class="['ai-chat-fab', isOpen ? 'fab-close' : 'fab-open']"
      :title="isOpen ? closeLabel : openLabel"
      aria-label="AI Yordamchi"
    >
      <!-- Chat icon -->
      <svg v-if="!isOpen" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
          d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-3 3-3-3z"/>
      </svg>
      <!-- Close icon -->
      <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
      </svg>
      <!-- Pulse ring (when closed) -->
      <span v-if="!isOpen" class="fab-pulse-ring"></span>
    </button>

    <!-- Chat window -->
    <Transition name="chat-window">
      <div v-if="isOpen" class="ai-chat-window">

        <!-- Header -->
        <div class="chat-header">
          <div class="chat-header-left">
            <div class="chat-avatar">
              <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17H3a2 2 0 01-2-2V5a2 2 0 012-2h14a2 2 0 012 2v10a2 2 0 01-2 2h-2"/>
              </svg>
            </div>
            <div>
              <p class="chat-title">{{ assistantName }}</p>
              <p class="chat-subtitle">
                <span class="online-dot"></span>{{ onlineLabel }}
              </p>
            </div>
          </div>
          <button @click="clearChat" :title="clearLabel" class="chat-clear-btn">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
            </svg>
          </button>
        </div>

        <!-- Messages -->
        <div ref="messagesEl" class="chat-messages">
          <!-- Welcome message -->
          <div class="msg-row msg-assistant">
            <div class="msg-bubble msg-bubble-assistant">
              <p>{{ welcomeMsg }}</p>
            </div>
          </div>

          <!-- Not configured notice -->
          <div v-if="!chatActive && !loading" class="msg-row msg-assistant">
            <div class="msg-bubble" style="background:#fff8e1;border:1px solid #fde68a;border-bottom-left-radius:4px;max-width:90%;font-size:13px;color:#92400e;">
              <p>⚙️ {{ notConfiguredText }}</p>
            </div>
          </div>

          <!-- History messages -->
          <div
            v-for="(msg, i) in messages"
            :key="i"
            :class="['msg-row', msg.role === 'user' ? 'msg-user' : 'msg-assistant']"
          >
            <div :class="['msg-bubble', msg.role === 'user' ? 'msg-bubble-user' : 'msg-bubble-assistant']">
              <p class="whitespace-pre-wrap">{{ msg.content }}</p>
            </div>
          </div>

          <!-- Typing indicator -->
          <div v-if="loading" class="msg-row msg-assistant">
            <div class="msg-bubble msg-bubble-assistant typing-indicator">
              <span></span><span></span><span></span>
            </div>
          </div>

          <!-- Error -->
          <div v-if="errorMsg" class="msg-row msg-assistant">
            <div class="msg-bubble msg-bubble-error">
              <p>{{ errorMsg }}</p>
            </div>
          </div>
        </div>

        <!-- Input -->
        <div class="chat-input-area">
          <textarea
            ref="inputEl"
            v-model="userInput"
            @keydown.enter.exact.prevent="sendMessage"
            :placeholder="inputPlaceholder"
            :disabled="loading"
            rows="1"
            class="chat-input"
            @input="autoResize"
          ></textarea>
          <button
            @click="sendMessage"
            :disabled="loading || !userInput.trim() || !chatActive"
            class="chat-send-btn"
            :title="sendLabel"
          >
            <svg v-if="!loading" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"/>
            </svg>
            <svg v-else class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/>
              <path class="opacity-75" fill="currentColor"
                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"/>
            </svg>
          </button>
        </div>
        <p class="chat-footer-note">Enter — yuborish &nbsp;|&nbsp; Shift+Enter — yangi qator</p>
      </div>
    </Transition>

  </div>
</template>

<script setup>
import { useRuntimeConfig } from '#imports'

const config = useRuntimeConfig()
const { currentLang } = useLanguage()

const isOpen     = ref(false)
const userInput  = ref('')
const messages   = ref([])   // [{role:'user'|'assistant', content:'...'}]
const loading    = ref(false)
const errorMsg   = ref('')
const chatActive = ref(false)
const chatConfig = ref(null)

const messagesEl = ref(null)
const inputEl    = ref(null)

// ── Fetch config ──────────────────────────────────
onMounted(async () => {
  try {
    const data = await $fetch(`${config.public.apiBase}/chat/config/`)
    chatActive.value = data.is_active
    chatConfig.value = data
  } catch (_) {
    chatActive.value = false
  }
})

// ── Labels ────────────────────────────────────────
const assistantName = computed(() => {
  if (currentLang.value === 'ru')    return 'AI Помощник'
  if (currentLang.value === 'uz_kr') return 'AI Ёрдамчи'
  return 'AI Yordamchi'
})
const onlineLabel = computed(() => {
  if (currentLang.value === 'ru')    return 'Onlayn'
  if (currentLang.value === 'uz_kr') return 'Онлайн'
  return 'Onlayn'
})
const openLabel = computed(() => {
  if (currentLang.value === 'ru')    return 'Открыть помощника'
  if (currentLang.value === 'uz_kr') return 'Ёрдамчини очиш'
  return 'Yordamchini ochish'
})
const closeLabel = computed(() => {
  if (currentLang.value === 'ru')    return 'Закрыть'
  if (currentLang.value === 'uz_kr') return 'Ёпиш'
  return 'Yopish'
})
const clearLabel = computed(() => {
  if (currentLang.value === 'ru')    return 'Очистить чат'
  if (currentLang.value === 'uz_kr') return 'Тозалаш'
  return 'Tozalash'
})
const inputPlaceholder = computed(() => {
  if (currentLang.value === 'ru')    return 'Напишите вопрос...'
  if (currentLang.value === 'uz_kr') return 'Саволингизни ёзинг...'
  return 'Savolingizni yozing...'
})
const sendLabel = computed(() => {
  if (currentLang.value === 'ru')    return 'Отправить'
  if (currentLang.value === 'uz_kr') return 'Юбориш'
  return 'Yuborish'
})
const welcomeMsg = computed(() => {
  if (!chatConfig.value) {
    if (currentLang.value === 'ru')    return 'Здравствуйте! Я AI помощник. Чем могу помочь?'
    if (currentLang.value === 'uz_kr') return 'Салом! Мен AI ёрдамчисиман. Қандай ёрдам бера оламан?'
    return "Salom! Men AI yordamchiman. Qanday yordam bera olaman?"
  }
  if (currentLang.value === 'ru')    return chatConfig.value.welcome_ru || chatConfig.value.welcome_uz
  if (currentLang.value === 'uz_kr') return chatConfig.value.welcome_kr || chatConfig.value.welcome_uz
  return chatConfig.value.welcome_uz
})

const notConfiguredText = computed(() => {
  if (currentLang.value === 'ru')    return 'AI сервис ещё не настроен. Пожалуйста, добавьте API ключ в панели администратора.'
  if (currentLang.value === 'uz_kr') return 'AI хизмат ҳали созланмаган. Илтимос, Admin panelda API калит қўшинг.'
  return "AI xizmat hali sozlanmagan. Admin panelda API kalit qo'shing."
})

// ── Actions ───────────────────────────────────────
function toggleChat() {
  isOpen.value = !isOpen.value
  if (isOpen.value) {
    nextTick(() => {
      scrollToBottom()
      inputEl.value?.focus()
    })
  }
}

function clearChat() {
  messages.value = []
  errorMsg.value = ''
}

async function sendMessage() {
  const text = userInput.value.trim()
  if (!text || loading.value) return

  messages.value.push({ role: 'user', content: text })
  userInput.value = ''
  errorMsg.value  = ''
  loading.value   = true

  // Reset textarea height
  if (inputEl.value) inputEl.value.style.height = 'auto'

  await nextTick()
  scrollToBottom()

  try {
    const data = await $fetch(`${config.public.apiBase}/chat/`, {
      method: 'POST',
      body: {
        message: text,
        history: messages.value.slice(0, -1),   // exclude the message we just added
      },
    })
    messages.value.push({ role: 'assistant', content: data.reply })
  } catch (err) {
    const msg = err?.data?.error || (currentLang.value === 'ru'
      ? 'Произошла ошибка. Попробуйте позже.'
      : 'Xatolik yuz berdi. Keyinroq urinib ko\'ring.')
    errorMsg.value = msg
  } finally {
    loading.value = false
    await nextTick()
    scrollToBottom()
  }
}

function scrollToBottom() {
  if (messagesEl.value) {
    messagesEl.value.scrollTop = messagesEl.value.scrollHeight
  }
}

function autoResize(e) {
  const el = e.target
  el.style.height = 'auto'
  el.style.height = Math.min(el.scrollHeight, 120) + 'px'
}
</script>

<style scoped>
/* ── Widget container ─────────────────────────── */
.ai-chat-widget {
  position: fixed;
  bottom: 24px;
  right: 24px;
  z-index: 9999;
  font-family: 'Inter', system-ui, sans-serif;
}

/* ── FAB button ──────────────────────────────── */
.ai-chat-fab {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  border: none;
  position: relative;
  transition: transform 0.2s, box-shadow 0.2s;
  box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}
.fab-open {
  background: rgb(var(--c-primary-600));
  color: #fff;
}
.fab-open:hover { transform: scale(1.08); }
.fab-close {
  background: #ef4444;
  color: #fff;
}
.fab-close:hover { transform: scale(1.08); }

.fab-pulse-ring {
  position: absolute;
  inset: -4px;
  border-radius: 50%;
  border: 2px solid rgb(var(--c-primary-400));
  animation: fab-pulse 2s infinite;
}
@keyframes fab-pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50%       { opacity: 0; transform: scale(1.4); }
}

/* ── Chat window ─────────────────────────────── */
.ai-chat-window {
  position: absolute;
  bottom: 68px;
  right: 0;
  width: 360px;
  max-height: 520px;
  background: #fff;
  border-radius: 20px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.18);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  border: 1px solid #e2e8f0;
}
@media (max-width: 480px) {
  .ai-chat-widget { bottom: 16px; right: 16px; }
  .ai-chat-window { width: calc(100vw - 32px); right: -8px; }
}

/* ── Header ──────────────────────────────────── */
.chat-header {
  background: linear-gradient(135deg, rgb(var(--c-primary-600)), rgb(var(--c-primary-700)));
  padding: 14px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-shrink: 0;
}
.chat-header-left { display: flex; align-items: center; gap: 10px; }
.chat-avatar {
  width: 36px; height: 36px;
  background: rgba(255,255,255,0.2);
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.chat-title { color: #fff; font-weight: 700; font-size: 14px; line-height: 1.2; }
.chat-subtitle { color: rgba(255,255,255,0.8); font-size: 12px; display: flex; align-items: center; gap: 5px; }
.online-dot {
  width: 8px; height: 8px;
  background: #4ade80;
  border-radius: 50%;
  display: inline-block;
  animation: blink 2s infinite;
}
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:.4} }
.chat-clear-btn {
  color: rgba(255,255,255,0.7);
  background: none; border: none; cursor: pointer;
  padding: 4px; border-radius: 6px; transition: color 0.2s;
}
.chat-clear-btn:hover { color: #fff; }

/* ── Messages ────────────────────────────────── */
.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 16px 14px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  background: #f8fafc;
  scroll-behavior: smooth;
}
.chat-messages::-webkit-scrollbar { width: 4px; }
.chat-messages::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 2px; }

.msg-row { display: flex; }
.msg-user      { justify-content: flex-end; }
.msg-assistant { justify-content: flex-start; }

.msg-bubble {
  max-width: 80%;
  padding: 9px 13px;
  border-radius: 16px;
  font-size: 13.5px;
  line-height: 1.55;
  word-break: break-word;
}
.msg-bubble-user {
  background: rgb(var(--c-primary-600));
  color: #fff;
  border-bottom-right-radius: 4px;
}
.msg-bubble-assistant {
  background: #fff;
  color: #1e293b;
  border: 1px solid #e2e8f0;
  border-bottom-left-radius: 4px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}
.msg-bubble-error {
  background: #fef2f2;
  color: #dc2626;
  border: 1px solid #fecaca;
  border-bottom-left-radius: 4px;
}

/* Typing dots */
.typing-indicator {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 12px 16px;
}
.typing-indicator span {
  width: 7px; height: 7px;
  background: #94a3b8;
  border-radius: 50%;
  display: inline-block;
  animation: typing 1.4s infinite ease-in-out;
}
.typing-indicator span:nth-child(1) { animation-delay: 0s; }
.typing-indicator span:nth-child(2) { animation-delay: 0.2s; }
.typing-indicator span:nth-child(3) { animation-delay: 0.4s; }
@keyframes typing {
  0%, 60%, 100% { transform: translateY(0); opacity: 0.5; }
  30%            { transform: translateY(-6px); opacity: 1; }
}

/* ── Input area ──────────────────────────────── */
.chat-input-area {
  display: flex;
  align-items: flex-end;
  gap: 8px;
  padding: 12px 14px;
  border-top: 1px solid #e2e8f0;
  background: #fff;
  flex-shrink: 0;
}
.chat-input {
  flex: 1;
  border: 1.5px solid #e2e8f0;
  border-radius: 12px;
  padding: 9px 12px;
  font-size: 13.5px;
  line-height: 1.5;
  resize: none;
  outline: none;
  transition: border-color 0.2s;
  max-height: 120px;
  overflow-y: auto;
  font-family: inherit;
  background: #f8fafc;
  color: #1e293b;
}
.chat-input:focus { border-color: rgb(var(--c-primary-500)); background: #fff; }
.chat-input:disabled { opacity: 0.6; }

.chat-send-btn {
  width: 40px; height: 40px; flex-shrink: 0;
  border-radius: 10px;
  background: rgb(var(--c-primary-600));
  color: #fff;
  border: none; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  transition: background 0.2s, transform 0.1s;
}
.chat-send-btn:hover:not(:disabled) {
  background: rgb(var(--c-primary-700));
  transform: scale(1.05);
}
.chat-send-btn:disabled { opacity: 0.5; cursor: default; }

.chat-footer-note {
  text-align: center;
  font-size: 11px;
  color: #94a3b8;
  padding: 0 14px 8px;
  background: #fff;
  flex-shrink: 0;
}

/* ── Window transition ───────────────────────── */
.chat-window-enter-active {
  animation: chat-in 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.chat-window-leave-active {
  animation: chat-out 0.18s ease-in;
}
@keyframes chat-in {
  from { opacity: 0; transform: scale(0.85) translateY(12px); transform-origin: bottom right; }
  to   { opacity: 1; transform: scale(1) translateY(0); }
}
@keyframes chat-out {
  from { opacity: 1; transform: scale(1); transform-origin: bottom right; }
  to   { opacity: 0; transform: scale(0.9) translateY(8px); }
}
</style>
