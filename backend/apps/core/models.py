from django.db import models


class GeneralInfo(models.Model):
    name_uz = models.CharField(max_length=255, verbose_name="Tashkilot nomi (O'z)")
    name_kr = models.CharField(max_length=255, verbose_name="Tashkilot nomi (Kr)", blank=True)
    name_ru = models.CharField(max_length=255, verbose_name="Tashkilot nomi (Ru)", blank=True)
    address_uz = models.TextField(verbose_name="Manzil (O'z)", default="")
    address_kr = models.TextField(verbose_name="Manzil (Kr)", blank=True)
    address_ru = models.TextField(verbose_name="Manzil (Ru)", blank=True)
    phone = models.CharField(max_length=50, verbose_name="Telefon raqami")
    hotline = models.CharField(max_length=50, verbose_name="Ishonch telefoni", blank=True)
    email = models.EmailField(verbose_name="Elektron pochta", blank=True)
    work_hours_uz = models.CharField(max_length=255, verbose_name="Ish vaqti (O'z)", blank=True)
    work_hours_kr = models.CharField(max_length=255, verbose_name="Ish vaqti (Kr)", blank=True)
    work_hours_ru = models.CharField(max_length=255, verbose_name="Ish vaqti (Ru)", blank=True)

    about_uz = models.TextField(verbose_name="Boshqarma haqida (O'z)", blank=True)
    about_kr = models.TextField(verbose_name="Boshqarma haqida (Kr)", blank=True)
    about_ru = models.TextField(verbose_name="Boshqarma haqida (Ru)", blank=True)

    history_uz = models.TextField(verbose_name="Boshqarma tarixi (O'z)", blank=True)
    history_kr = models.TextField(verbose_name="Boshqarma tarixi (Kr)", blank=True)
    history_ru = models.TextField(verbose_name="Boshqarma tarixi (Ru)", blank=True)

    statute_link = models.URLField(verbose_name="Nizom havolasi (URL)", blank=True)

    telegram = models.URLField(blank=True, verbose_name="Telegram")
    facebook = models.URLField(blank=True, verbose_name="Facebook")
    instagram = models.URLField(blank=True, verbose_name="Instagram")
    youtube = models.URLField(blank=True, verbose_name="YouTube")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Umumiy ma'lumot"
        verbose_name_plural = "Umumiy ma'lumotlar"

    def __str__(self):
        return self.name_uz


class SiteSettings(models.Model):
    primary_color = models.CharField(max_length=7, default="#0ea5e9", verbose_name="Asosiy rang (primary)")
    secondary_color = models.CharField(max_length=7, default="#14b8a6", verbose_name="Ikkinchi rang (secondary)")
    accent_color = models.CharField(max_length=7, default="#f59e0b", verbose_name="Aksent rang")
    logo = models.ImageField(upload_to="site/", verbose_name="Sayt logotipi", blank=True, null=True)
    favicon = models.ImageField(upload_to="site/", verbose_name="Favicon", blank=True, null=True)

    class Meta:
        verbose_name = "Sayt sozlamalari"
        verbose_name_plural = "Sayt sozlamalari"

    def __str__(self):
        return "Sayt sozlamalari"


class Banner(models.Model):
    title_uz = models.CharField(max_length=255, verbose_name="Sarlavha (O'z)")
    title_kr = models.CharField(max_length=255, verbose_name="Sarlavha (Kr)", blank=True)
    title_ru = models.CharField(max_length=255, verbose_name="Sarlavha (Ru)", blank=True)
    subtitle_uz = models.CharField(max_length=255, verbose_name="Qo'shimcha sarlavha (O'z)", blank=True)
    subtitle_kr = models.CharField(max_length=255, verbose_name="Qo'shimcha sarlavha (Kr)", blank=True)
    subtitle_ru = models.CharField(max_length=255, verbose_name="Qo'shimcha sarlavha (Ru)", blank=True)
    description_uz = models.TextField(verbose_name="Tavsif (O'z)", blank=True)
    description_kr = models.TextField(verbose_name="Tavsif (Kr)", blank=True)
    description_ru = models.TextField(verbose_name="Tavsif (Ru)", blank=True)
    image = models.ImageField(upload_to="banners/", verbose_name="Rasm")
    link = models.CharField(max_length=255, verbose_name="Havola", blank=True)
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    is_active = models.BooleanField(default=True, verbose_name="Faol")

    class Meta:
        verbose_name = "Bosh sahifa banneri"
        verbose_name_plural = "Bosh sahifa bannerlari"
        ordering = ["order"]

    def __str__(self):
        return self.title_uz


class NavItem(models.Model):
    label_uz = models.CharField(max_length=100, verbose_name="Nomi (O'z)")
    label_kr = models.CharField(max_length=100, verbose_name="Nomi (Kr)", blank=True)
    label_ru = models.CharField(max_length=100, verbose_name="Nomi (Ru)", blank=True)
    url = models.CharField(max_length=255, verbose_name="Havola (masalan: /about)")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    is_active = models.BooleanField(default=True, verbose_name="Faol")

    class Meta:
        verbose_name = "Yuqori menyu havolasi"
        verbose_name_plural = "Yuqori menyu havolalari"
        ordering = ["order"]

    def __str__(self):
        return self.label_uz


class FooterLink(models.Model):
    COLUMN_CHOICES = (
        ('quick', "Tezkor havolalar"),
        ('gov', "Davlat saytlari"),
    )
    column = models.CharField(max_length=10, choices=COLUMN_CHOICES, default='quick', verbose_name="Bo'lim")
    label_uz = models.CharField(max_length=100, verbose_name="Nomi (O'z)")
    label_kr = models.CharField(max_length=100, verbose_name="Nomi (Kr)", blank=True)
    label_ru = models.CharField(max_length=100, verbose_name="Nomi (Ru)", blank=True)
    url = models.CharField(max_length=255, verbose_name="Havola")
    is_external = models.BooleanField(default=False, verbose_name="Tashqi havola")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    is_active = models.BooleanField(default=True, verbose_name="Faol")

    class Meta:
        verbose_name = "Pastki menyu havolasi"
        verbose_name_plural = "Pastki menyu havolalari"
        ordering = ["column", "order"]

    def __str__(self):
        return f"{self.get_column_display()} — {self.label_uz}"


class PageSection(models.Model):
    SECTION_TYPES = (
        ('text', 'Matn bloki'),
        ('cards', 'Kartochkalar'),
        ('stats', 'Statistika'),
        ('cta', "Chaqiruv (CTA)"),
    )
    page = models.CharField(max_length=50, default='home', verbose_name="Sahifa (masalan: home)")
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES, default='text', verbose_name="Bo'lim turi")
    title_uz = models.CharField(max_length=255, verbose_name="Sarlavha (O'z)")
    title_kr = models.CharField(max_length=255, verbose_name="Sarlavha (Kr)", blank=True)
    title_ru = models.CharField(max_length=255, verbose_name="Sarlavha (Ru)", blank=True)
    content_uz = models.TextField(verbose_name="Matn (O'z)", blank=True)
    content_kr = models.TextField(verbose_name="Matn (Kr)", blank=True)
    content_ru = models.TextField(verbose_name="Matn (Ru)", blank=True)
    image = models.ImageField(upload_to="sections/", verbose_name="Rasm", blank=True, null=True)
    extra_data = models.JSONField(default=dict, blank=True, verbose_name="Qo'shimcha ma'lumot (JSON)")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    is_active = models.BooleanField(default=True, verbose_name="Faol")

    class Meta:
        verbose_name = "Sahifa bo'limi"
        verbose_name_plural = "Sahifa bo'limlari"
        ordering = ["page", "order"]

    def __str__(self):
        return f"{self.page} — {self.title_uz}"


class SectionCard(models.Model):
    section = models.ForeignKey(PageSection, on_delete=models.CASCADE, related_name="cards", verbose_name="Bo'lim")
    title_uz = models.CharField(max_length=255, verbose_name="Sarlavha (O'z)")
    title_kr = models.CharField(max_length=255, verbose_name="Sarlavha (Kr)", blank=True)
    title_ru = models.CharField(max_length=255, verbose_name="Sarlavha (Ru)", blank=True)
    text_uz = models.TextField(verbose_name="Matn (O'z)", blank=True)
    text_kr = models.TextField(verbose_name="Matn (Kr)", blank=True)
    text_ru = models.TextField(verbose_name="Matn (Ru)", blank=True)
    icon = models.CharField(max_length=50, verbose_name="Ikonka nomi", blank=True)
    image = models.ImageField(upload_to="cards/", verbose_name="Rasm", blank=True, null=True)
    link = models.CharField(max_length=255, verbose_name="Havola", blank=True)
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")

    class Meta:
        verbose_name = "Kartochka"
        verbose_name_plural = "Kartochkalar"
        ordering = ["order"]

    def __str__(self):
        return self.title_uz


class CustomPage(models.Model):
    """Dinamik sahifalar — admin paneldan yangi sahifa yaratish uchun."""
    slug = models.SlugField(
        max_length=100, unique=True,
        verbose_name="URL manzil (slug)",
        help_text="Faqat lotin harflari, raqamlar va '-' belgisi. Masalan: xizmatlar, bolalar-salomatligi"
    )
    title_uz = models.CharField(max_length=255, verbose_name="Sarlavha (O'z)")
    title_kr = models.CharField(max_length=255, blank=True, verbose_name="Sarlavha (Kr)")
    title_ru = models.CharField(max_length=255, blank=True, verbose_name="Sarlavha (Ru)")
    meta_description_uz = models.CharField(
        max_length=300, blank=True,
        verbose_name="Meta tavsif (O'z)",
        help_text="Qidiruv tizimlarida ko'rinadigan qisqa tavsif (150–160 belgi)"
    )
    show_in_nav = models.BooleanField(
        default=False, verbose_name="Asosiy menyuga qo'shish",
        help_text="Belgilansa, bu sahifa yuqori navigatsiya menyusida avtomatik paydo bo'ladi"
    )
    nav_order = models.PositiveIntegerField(
        default=99, verbose_name="Menyu tartib raqami",
        help_text="Menyudagi o'rni (kichik son = oldinda)"
    )
    is_active = models.BooleanField(default=True, verbose_name="Faol (saytda ko'rinadi)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Maxsus sahifa"
        verbose_name_plural = "Maxsus sahifalar"
        ordering = ['slug']

    def __str__(self):
        return f"{self.title_uz}  (/{self.slug})"


class CustomPageBlock(models.Model):
    """Sahifa ichidagi kontent bloklari."""
    BLOCK_TYPES = (
        ('text',       'Matn bloki'),
        ('image_text', 'Rasm + Matn'),
        ('cards',      'Kartochkalar'),
        ('cta',        'Chaqiruv tugmasi (CTA)'),
        ('divider',    'Bo\'luvchi chiziq'),
    )
    IMAGE_POSITION = (
        ('right', "O'ngda"),
        ('left',  "Chapda"),
    )
    page = models.ForeignKey(
        CustomPage, on_delete=models.CASCADE,
        related_name='blocks', verbose_name="Sahifa"
    )
    block_type = models.CharField(
        max_length=20, choices=BLOCK_TYPES, default='text',
        verbose_name="Blok turi"
    )
    title_uz = models.CharField(max_length=255, blank=True, verbose_name="Sarlavha (O'z)")
    title_kr = models.CharField(max_length=255, blank=True, verbose_name="Sarlavha (Kr)")
    title_ru = models.CharField(max_length=255, blank=True, verbose_name="Sarlavha (Ru)")
    content_uz = models.TextField(
        blank=True, verbose_name="Matn (O'z)",
        help_text="HTML teglarini ishlatish mumkin: &lt;b&gt;, &lt;i&gt;, &lt;br&gt;, &lt;ul&gt;&lt;li&gt;..."
    )
    content_kr = models.TextField(blank=True, verbose_name="Matn (Kr)")
    content_ru = models.TextField(blank=True, verbose_name="Matn (Ru)")
    image = models.ImageField(
        upload_to='pages/', blank=True, null=True,
        verbose_name="Rasm",
        help_text="'Rasm + Matn' bloki uchun. Tavsiya: 800×500 px"
    )
    image_position = models.CharField(
        max_length=10, choices=IMAGE_POSITION, default='right',
        verbose_name="Rasm joylashuvi",
        help_text="'Rasm + Matn' blokida rasm matnning qaysi tomonida turadi"
    )
    link_text_uz = models.CharField(max_length=100, blank=True, verbose_name="Tugma matni (O'z)")
    link_text_kr = models.CharField(max_length=100, blank=True, verbose_name="Tugma matni (Kr)")
    link_text_ru = models.CharField(max_length=100, blank=True, verbose_name="Tugma matni (Ru)")
    link_url = models.CharField(
        max_length=255, blank=True, verbose_name="Tugma havolasi",
        help_text="Masalan: /contact  yoki  https://gov.uz"
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    is_active = models.BooleanField(default=True, verbose_name="Faol")

    class Meta:
        verbose_name = "Sahifa bloki"
        verbose_name_plural = "Sahifa bloklari"
        ordering = ['page', 'order']

    def __str__(self):
        return f"{self.page.title_uz} — {self.get_block_type_display()} (#{self.order})"


class CustomPageCard(models.Model):
    """Kartochkalar bloki ichidagi alohida kartochkalar."""
    block = models.ForeignKey(
        CustomPageBlock, on_delete=models.CASCADE,
        related_name='cards', verbose_name="Blok"
    )
    title_uz = models.CharField(max_length=255, verbose_name="Sarlavha (O'z)")
    title_kr = models.CharField(max_length=255, blank=True, verbose_name="Sarlavha (Kr)")
    title_ru = models.CharField(max_length=255, blank=True, verbose_name="Sarlavha (Ru)")
    text_uz = models.TextField(blank=True, verbose_name="Matn (O'z)")
    text_kr = models.TextField(blank=True, verbose_name="Matn (Kr)")
    text_ru = models.TextField(blank=True, verbose_name="Matn (Ru)")
    icon = models.CharField(
        max_length=50, blank=True, verbose_name="Ikonka",
        help_text="Emoji (masalan: 🏥) yoki fon-awesome klass (fa-heart)"
    )
    image = models.ImageField(
        upload_to='pages/cards/', blank=True, null=True, verbose_name="Rasm"
    )
    link = models.CharField(max_length=255, blank=True, verbose_name="Havola")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")

    class Meta:
        verbose_name = "Kartochka"
        verbose_name_plural = "Kartochkalar"
        ordering = ['order']

    def __str__(self):
        return self.title_uz


class MediaAsset(models.Model):
    LOCATION_CHOICES = (
        ('hero', "Bosh sahifa fon rasmi"),
        ('about', "Biz haqimizda rasm"),
        ('contact', "Aloqa sahifasi rasmi"),
        ('other', "Boshqa"),
    )
    name = models.CharField(max_length=100, verbose_name="Nomi")
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES, default='other', verbose_name="Joylashuvi")
    image = models.ImageField(upload_to="assets/", verbose_name="Rasm")
    alt_text = models.CharField(max_length=255, verbose_name="Alt matn", blank=True)

    class Meta:
        verbose_name = "Sayt rasmi"
        verbose_name_plural = "Sayt rasmlari"

    def __str__(self):
        return f"{self.name} ({self.get_location_display()})"
