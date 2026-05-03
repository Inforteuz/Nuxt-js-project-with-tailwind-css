from django.db import models


class AIConfig(models.Model):
    """Sayt uchun faol AI yordamchi sozlamalari."""

    PROVIDER_CHOICES = (
        ('openai',      'OpenAI (GPT-4o, GPT-4o-mini...)'),
        ('gemini',      'Google Gemini (gemini-1.5-flash...)'),
        ('openrouter',  'OpenRouter (ko\'plab modellar)'),
        ('groq',        'Groq (Llama, Mixtral...)'),
    )

    provider = models.CharField(
        max_length=20, choices=PROVIDER_CHOICES, default='openai',
        verbose_name="AI xizmat provayderi",
        help_text="Qaysi AI xizmatidan foydalanishni tanlang"
    )
    api_key = models.CharField(
        max_length=500,
        verbose_name="API kalit (API Key)",
        help_text="Tanlangan provayder saytidan olingan maxfiy kalit"
    )
    model_name = models.CharField(
        max_length=100,
        verbose_name="Model nomi",
        help_text=(
            "OpenAI: gpt-4o-mini, gpt-4o | "
            "Gemini: gemini-1.5-flash, gemini-1.5-pro | "
            "OpenRouter: mistralai/mistral-7b-instruct | "
            "Groq: llama3-8b-8192"
        ),
        default='gpt-4o-mini',
    )
    system_prompt = models.TextField(
        verbose_name="Tizim xabari (System Prompt)",
        default=(
            "Siz sayt foydalanuvchilariga yordam beruvchi AI yordamchisiz. "
            "Samarali, qisqa va aniq javoblar bering. "
            "Faqat quyidagi ma'lumotlar asosida javob bering."
        ),
        help_text=(
            "AI yordamchining xulq-atvori va yo'riqnomasi. "
            "Masalan: qaysi tashkilot haqida, qanday murojaat qilish mumkin, qaysi xizmatlar bor."
        )
    )
    temperature = models.FloatField(
        default=0.7,
        verbose_name="Ijodkorlik darajasi (0.0 – 1.0)",
        help_text="0.0 = aniq/qattiq, 1.0 = ijodiy/erkin"
    )
    max_tokens = models.PositiveIntegerField(
        default=800,
        verbose_name="Maksimal javob uzunligi (tokenlar)",
        help_text="1 token ≈ 4 harif. 800 token ≈ 600 so'z"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Faol (saytda ko'rinadi)",
        help_text="Belgilansa, saytda chat tugmasi paydo bo'ladi"
    )
    welcome_message_uz = models.CharField(
        max_length=300,
        verbose_name="Salomlashuv xabari (O'z)",
        default="Salom! Men sayt yordamchisiman. Qanday yordam bera olaman?",
    )
    welcome_message_ru = models.CharField(
        max_length=300,
        verbose_name="Salomlashuv xabari (Ru)",
        default="Здравствуйте! Я помощник сайта. Чем могу помочь?",
        blank=True,
    )
    welcome_message_kr = models.CharField(
        max_length=300,
        verbose_name="Salomlashuv xabari (Kr)",
        default="Салом! Мен сайт ёрдамчисиман. Қандай ёрдам бера оламан?",
        blank=True,
    )

    class Meta:
        verbose_name = "AI Yordamchi sozlamalari"
        verbose_name_plural = "AI Yordamchi sozlamalari"

    def __str__(self):
        return f"{self.get_provider_display()} — {self.model_name}"


class KnowledgeItem(models.Model):
    """AI yordamchi biladigan ma'lumotlar bazasi."""

    CATEGORY_CHOICES = (
        ('general',   'Umumiy ma\'lumot'),
        ('services',  'Xizmatlar'),
        ('contacts',  'Aloqa ma\'lumotlari'),
        ('faq',       'Ko\'p so\'raladigan savollar'),
        ('procedure', 'Qabul tartibi / Murojaat'),
        ('other',     'Boshqa'),
    )

    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default='general',
        verbose_name="Kategoriya"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Mavzu / Sarlavha",
        help_text="Masalan: Qabul vaqti, Manzil, Bolalar shifokoriga murojaat"
    )
    content = models.TextField(
        verbose_name="Ma'lumot matni",
        help_text=(
            "AI shu ma'lumotga tayangan holda javob beradi. "
            "Aniq va to'liq yozing. Tilni aralashtirishingiz mumkin."
        )
    )
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")

    class Meta:
        verbose_name = "Bilimlar bazasi yozuvi"
        verbose_name_plural = "Bilimlar bazasi"
        ordering = ['category', 'order']

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title}"
