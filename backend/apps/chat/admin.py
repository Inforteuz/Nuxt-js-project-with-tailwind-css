from django.contrib import admin
from django.utils.html import format_html, mark_safe
from .models import AIConfig, KnowledgeItem


@admin.register(AIConfig)
class AIConfigAdmin(admin.ModelAdmin):
    list_display = ('provider_badge', 'model_name', 'is_active', 'status_indicator')
    list_editable = ('is_active',)

    fieldsets = (
        ("Provayder va API kalit", {
            'description': mark_safe(
                '<div style="background:#e8f5e9;color:#444;padding:12px 16px;border-radius:8px;'
                'margin-bottom:12px;font-size:13px;line-height:1.7;">'
                '<b>Sozlash tartibi:</b><br>'
                '1. Provayderni tanlang (masalan: OpenAI yoki Groq)<br>'
                '2. O\'sha provayder saytidan API kalit oling<br>'
                '3. Model nomini kiriting (namuna: <code>gpt-4o-mini</code>)<br>'
                '4. Tizim xabarini yozing<br>'
                '5. «Saqlash» tugmasini bosing<br><br>'
                '<b>Provayder API kalit olish sahifalari:</b><br>'
                'OpenAI: <code>platform.openai.com/api-keys</code><br>'
                'Gemini: <code>aistudio.google.com/app/apikey</code><br>'
                'OpenRouter: <code>openrouter.ai/keys</code><br>'
                'Groq: <code>console.groq.com/keys</code>'
                '</div>'
            ),
            'fields': ('provider', 'api_key', 'model_name'),
        }),
        ("Chatbot xulq-atvori", {
            'description': mark_safe(
                '<p class="help">'
                'Tizim xabari AI yordamchining xulqini belgilaydi. '
                'Quyida bilimlar bazasidan olingan ma\'lumotlar avtomatik qo\'shiladi.'
                '</p>'
            ),
            'fields': ('system_prompt', 'temperature', 'max_tokens'),
        }),
        ("Salomlashuv xabarlari", {
            'fields': ('welcome_message_uz', 'welcome_message_ru', 'welcome_message_kr'),
        }),
        ("Holat", {
            'fields': ('is_active',),
        }),
    )

    def provider_badge(self, obj):
        colors = {
            'openai': '#10a37f',
            'gemini': '#4285f4',
            'openrouter': '#7c3aed',
            'groq': '#f97316',
        }
        color = colors.get(obj.provider, '#64748b')
        return format_html(
            '<span style="background:{};color:#fff;padding:2px 10px;'
            'border-radius:12px;font-size:12px;font-weight:600;">{}</span>',
            color, obj.get_provider_display().split(' ')[0]
        )
    provider_badge.short_description = "Provayder"

    def status_indicator(self, obj):
        if obj.is_active:
            return format_html(
                '<span style="color:#10b981;font-weight:600;">Faol</span>'
            )
        return format_html('<span style="color:#94a3b8;">O\'chiq</span>')
    status_indicator.short_description = "Holat"

    def has_add_permission(self, request):
        return not AIConfig.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['subtitle'] = (
            "AI yordamchi sozlamalari. Bir vaqtda faqat bitta konfiguratsiya faol bo'lishi mumkin. "
            "API kalitni kiriting va chatbot saytda paydo bo'ladi."
        )
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(KnowledgeItem)
class KnowledgeItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category_badge', 'content_preview', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('category', 'is_active')
    list_display_links = ('title',)
    search_fields = ('title', 'content')

    fields = ('category', 'title', 'content', 'order', 'is_active')

    def category_badge(self, obj):
        colors = {
            'general':   '#0ea5e9',
            'services':  '#10b981',
            'contacts':  '#f59e0b',
            'faq':       '#8b5cf6',
            'procedure': '#ef4444',
            'other':     '#64748b',
        }
        color = colors.get(obj.category, '#64748b')
        return format_html(
            '<span style="background:{};color:#fff;padding:2px 8px;'
            'border-radius:10px;font-size:11px;">{}</span>',
            color, obj.get_category_display()
        )
    category_badge.short_description = "Kategoriya"

    def content_preview(self, obj):
        preview = obj.content[:80] + ('...' if len(obj.content) > 80 else '')
        return format_html('<span style="color:#64748b;">{}</span>', preview)
    content_preview.short_description = "Ma'lumot"

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['subtitle'] = mark_safe(
            'AI yordamchi shu ma\'lumotlar asosida javob beradi. '
            'Qanchalik ko\'p va aniq ma\'lumot kiritsangiz, shunchalik yaxshi javob olasiz.<br>'
            '<b>Maslahat:</b> Qabul vaqti, manzil, telefon, xizmatlar ro\'yxati, tez-tez '
            'so\'raladigan savollar — bularni yaxshilab to\'ldiring.'
        )
        return super().changelist_view(request, extra_context=extra_context)
