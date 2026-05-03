from django import forms
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.html import format_html, mark_safe
from django.urls import reverse
from .models import (
    GeneralInfo, SiteSettings, Banner, NavItem,
    FooterLink, PageSection, SectionCard, MediaAsset,
    CustomPage, CustomPageBlock, CustomPageCard,
)

admin.site.site_header = f"{settings.SITE_NAME} — Boshqaruv paneli"
admin.site.site_title = f"{settings.SITE_ABBR} Admin"
admin.site.index_title = "Saytni boshqarish"

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')

    def has_module_permission(self, request):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(Group)
class CustomGroupAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return request.user.is_superuser


# ---- Color picker ----
class ColorPickerWidget(forms.TextInput):
    input_type = 'color'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs.update({
            'style': 'width:70px;height:42px;padding:2px 4px;cursor:pointer;border-radius:6px;'
        })


class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = '__all__'
        widgets = {
            'primary_color': ColorPickerWidget(),
            'secondary_color': ColorPickerWidget(),
            'accent_color': ColorPickerWidget(),
        }


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    form = SiteSettingsForm
    list_display = ('__str__', 'primary_color_preview', 'secondary_color_preview', 'accent_color_preview')

    fieldsets = (
        ("Sayt ranglari", {
            'description': mark_safe(
                '<div class="help" style="background:#fff3cd;padding:10px 14px;border-radius:6px;margin-bottom:8px;font-size:13px;">'
                '<b>Rangni qanday o\'zgartirish:</b> quyidagi rangli kvadratni bosing → palitra ochiladi → rang tanlang → Saqlash.<br>'
                'Asosiy rang — navbar va tugmalar rangi. &nbsp; Ikkinchi rang — kategoriya va hover effektlar. &nbsp; Aksent rang — muhim belgilar.'
                '</div>'
            ),
            'fields': ('primary_color', 'secondary_color', 'accent_color'),
        }),
        ("Logotip va Favicon", {
            'description': mark_safe(
                '<p class="help">Logotip — navbar yuqori chap burchagida ko\'rinadi (PNG tavsiya, 240×60 px). '
                'Favicon — brauzer tabidagi kichik ikonka (32×32 px).</p>'
            ),
            'fields': ('logo', 'favicon'),
        }),
    )

    def primary_color_preview(self, obj):
        return format_html(
            '<span style="display:inline-block;width:22px;height:22px;background:{};'
            'border-radius:50%;border:2px solid #ddd;vertical-align:middle;margin-right:6px;"></span>'
            '<code>{}</code>', obj.primary_color, obj.primary_color
        )
    primary_color_preview.short_description = "Asosiy rang"

    def secondary_color_preview(self, obj):
        return format_html(
            '<span style="display:inline-block;width:22px;height:22px;background:{};'
            'border-radius:50%;border:2px solid #ddd;vertical-align:middle;margin-right:6px;"></span>'
            '<code>{}</code>', obj.secondary_color, obj.secondary_color
        )
    secondary_color_preview.short_description = "Ikkinchi rang"

    def accent_color_preview(self, obj):
        return format_html(
            '<span style="display:inline-block;width:22px;height:22px;background:{};'
            'border-radius:50%;border:2px solid #ddd;vertical-align:middle;margin-right:6px;"></span>'
            '<code>{}</code>', obj.accent_color, obj.accent_color
        )
    accent_color_preview.short_description = "Aksent rang"

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'phone', 'email')

    fieldsets = (
        ("Tashkilot nomi", {
            'description': mark_safe('<p class="help">Sayt sarlavhasi, navbar va footerda ko\'rinadigan rasmiy nom.</p>'),
            'fields': ('name_uz', 'name_kr', 'name_ru'),
        }),
        ("Aloqa ma'lumotlari", {
            'description': mark_safe('<p class="help">Header yuqorisidagi telefon/email va Aloqa sahifasida ko\'rinadi.</p>'),
            'fields': ('address_uz', 'address_kr', 'address_ru', 'phone', 'hotline', 'email'),
        }),
        ("Ish vaqti", {
            'fields': ('work_hours_uz', 'work_hours_kr', 'work_hours_ru'),
        }),
        ("Boshqarma haqida", {
            'description': mark_safe('<p class="help">«Biz haqimizda» sahifasining asosiy matni.</p>'),
            'fields': ('about_uz', 'about_kr', 'about_ru'),
        }),
        ("Boshqarma tarixi", {
            'classes': ('collapse',),
            'fields': ('history_uz', 'history_kr', 'history_ru'),
        }),
        ("Nizom", {
            'description': mark_safe('<p class="help">«Biz haqimizda» sahifasidagi «Nizomni yuklab olish» tugmasi havolasi.</p>'),
            'fields': ('statute_link',),
        }),
        ("Ijtimoiy tarmoqlar", {
            'description': mark_safe('<p class="help">Footer pastki qismidagi ijtimoiy tarmoq havolalari.</p>'),
            'fields': ('telegram', 'facebook', 'instagram', 'youtube'),
        }),
    )

    def has_add_permission(self, request):
        return not GeneralInfo.objects.exists()


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'image_preview', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_display_links = ('title_uz',)

    fieldsets = (
        ("Sarlavha", {
            'description': mark_safe(
                '<p class="help">Bosh sahifadagi karusel banneri sarlavhasi — bannerning markazida katta harflar bilan ko\'rinadi.</p>'
            ),
            'fields': ('title_uz', 'title_kr', 'title_ru'),
        }),
        ("Qo'shimcha sarlavha", {
            'fields': ('subtitle_uz', 'subtitle_kr', 'subtitle_ru'),
        }),
        ("Tavsif", {
            'fields': ('description_uz', 'description_kr', 'description_ru'),
        }),
        ("Rasm va havola", {
            'description': mark_safe(
                '<p class="help">Tavsiya etilgan rasm o\'lchami: 1920×700 px. '
                'Havola: masalan <code>/about</code> yoki <code>https://...</code></p>'
            ),
            'fields': ('image', 'link'),
        }),
        ("Sozlamalar", {
            'fields': ('order', 'is_active'),
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:40px;border-radius:4px;"/>', obj.image.url)
        return "—"
    image_preview.short_description = "Rasm"


@admin.register(NavItem)
class NavItemAdmin(admin.ModelAdmin):
    list_display = ('label_uz', 'url', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    fields = ('label_uz', 'label_kr', 'label_ru', 'url', 'order', 'is_active')

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['subtitle'] = mark_safe(
            'Saytning yuqori navigatsiya menyusi. '
            'Havola misollari: <code>/news</code>, <code>/about</code>, <code>/contact</code>. '
            'Tartib raqami kichikroq bo\'lsa — menyuda oldinda ko\'rinadi.'
        )
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ('label_uz', 'column', 'url', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('column',)
    fields = ('column', 'label_uz', 'label_kr', 'label_ru', 'url', 'is_external', 'order', 'is_active')

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['subtitle'] = (
            "Sayt pastki qismi (footer) havolalari. "
            "'Tezkor havolalar' — ichki sahifalar. "
            "'Davlat saytlari' — tashqi davlat portallari. "
            "'Tashqi havola' belgisi qo'yilsa yangi oynada ochiladi."
        )
        return super().changelist_view(request, extra_context=extra_context)


class SectionCardInline(admin.StackedInline):
    model = SectionCard
    extra = 1
    fields = ('title_uz', 'title_kr', 'title_ru', 'text_uz', 'text_kr', 'text_ru', 'icon', 'image', 'link', 'order')


@admin.register(PageSection)
class PageSectionAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'page', 'section_type', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('page', 'section_type')
    inlines = [SectionCardInline]

    fieldsets = (
        ("Asosiy sozlamalar", {
            'description': mark_safe(
                '<p class="help">'
                'Sahifa: <code>home</code> = Bosh sahifa, <code>about</code> = Biz haqimizda. &nbsp; '
                'Bo\'lim turi: Matn bloki / Kartochkalar / Statistika / Chaqiruv.'
                '</p>'
            ),
            'fields': ('page', 'section_type', 'order', 'is_active'),
        }),
        ("Sarlavha", {'fields': ('title_uz', 'title_kr', 'title_ru')}),
        ("Matn", {'fields': ('content_uz', 'content_kr', 'content_ru')}),
        ("Rasm", {'fields': ('image',)}),
        ("Qo'shimcha ma'lumot", {'fields': ('extra_data',), 'classes': ('collapse',)}),
    )


@admin.register(MediaAsset)
class MediaAssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'image_preview', 'alt_text')
    list_filter = ('location',)
    fields = ('name', 'location', 'image', 'alt_text')

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['subtitle'] = (
            "Saytning asosiy rasmlari. "
            "Joylashuvni tanlang: 'Bosh sahifa fon rasmi' — hero section, "
            "'Biz haqimizda rasm' — about sahifasi, "
            "'Aloqa sahifasi rasmi' — contact sahifasi."
        )
        return super().changelist_view(request, extra_context=extra_context)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px;border-radius:6px;"/>', obj.image.url)
        return "—"
    image_preview.short_description = "Ko'rinish"


# ─────────────────────────────────────────────
#  CUSTOM PAGES
# ─────────────────────────────────────────────

class CustomPageBlockInline(admin.TabularInline):
    model = CustomPageBlock
    extra = 1
    fields = ('block_type', 'title_uz', 'image', 'order', 'is_active', 'edit_link')
    readonly_fields = ('edit_link',)
    show_change_link = False
    verbose_name = "Blok"
    verbose_name_plural = mark_safe(
        "Kontent bloklari &nbsp;"
        "<small style='font-weight:normal;color:#888;'>"
        "— blokni to'liq tahrirlash uchun uning nomini bosing.</small>"
    )

    def edit_link(self, obj):
        if obj.pk:
            url = reverse('admin:core_custompageblock_change', args=[obj.pk])
            return format_html(
                '<a href="{}" target="_blank" style="white-space:nowrap;">'
                'To\'liq tahrirlash &rarr;</a>', url
            )
        return mark_safe('<span style="color:#aaa;">Avval saqlang</span>')
    edit_link.short_description = "Tahrirlash"


@admin.register(CustomPage)
class CustomPageAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'slug_link', 'show_in_nav', 'nav_order', 'blocks_count', 'is_active', 'updated_at')
    list_editable = ('show_in_nav', 'nav_order', 'is_active')
    list_display_links = ('title_uz',)
    search_fields = ('title_uz', 'title_ru', 'slug')
    prepopulated_fields = {'slug': ('title_uz',)}
    inlines = [CustomPageBlockInline]

    fieldsets = (
        ("Sahifa nomi va manzili", {
            'description': mark_safe(
                '<div style="background:#e8f4ff;padding:10px 14px;border-radius:6px;'
                'margin-bottom:10px;font-size:13px;line-height:1.6;">'
                '<b>Yangi sahifa yaratish:</b><br>'
                '1. Sarlavhani yozing — slug avtomatik to\'ldiriladi.<br>'
                '2. «Saqlash va davom etish» tugmasini bosing.<br>'
                '3. Pastdagi «Blok qo\'shish» orqali kontent qo\'shing.<br>'
                '4. Menyuga qo\'shish uchun «Asosiy menyuga qo\'shish» belgisini qo\'ying.'
                '</div>'
            ),
            'fields': ('title_uz', 'title_kr', 'title_ru', 'slug'),
        }),
        ("SEO va navigatsiya", {
            'fields': ('meta_description_uz', 'show_in_nav', 'nav_order', 'is_active'),
        }),
    )

    def slug_link(self, obj):
        return format_html(
            '<code style="background:#f0f4ff;padding:2px 6px;border-radius:4px;">/{}</code>',
            obj.slug
        )
    slug_link.short_description = "URL"

    def blocks_count(self, obj):
        n = obj.blocks.filter(is_active=True).count()
        total = obj.blocks.count()
        return format_html(
            '<span style="color:{};font-weight:bold;">{}</span>'
            '<span style="color:#aaa;"> / {}</span>',
            '#059669' if n > 0 else '#dc2626', n, total
        )
    blocks_count.short_description = "Faol bloklar"

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['subtitle'] = mark_safe(
            'Bu yerda yangi sahifalar yarating — har bir sahifa o\'z URL manziliga ega bo\'ladi '
            '(masalan: <code>/xizmatlar</code>, <code>/bolalar-salomatligi</code>). '
            'Sahifani yaratgach, unga kontent bloklari qo\'shing.'
        )
        return super().changelist_view(request, extra_context=extra_context)


class CustomPageCardInline(admin.StackedInline):
    model = CustomPageCard
    extra = 1
    fields = ('title_uz', 'title_kr', 'title_ru',
              'text_uz', 'text_kr', 'text_ru',
              'icon', 'image', 'link', 'order')
    verbose_name = "Kartochka"
    verbose_name_plural = "Kartochkalar"


@admin.register(CustomPageBlock)
class CustomPageBlockAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'page_link', 'block_type', 'order', 'is_active')
    list_filter = ('page', 'block_type')
    list_editable = ('order', 'is_active')
    list_display_links = ('__str__',)
    inlines = [CustomPageCardInline]

    fieldsets = (
        ("Asosiy", {
            'description': mark_safe(
                '<div style="background:#fff8e1;padding:10px 14px;border-radius:6px;'
                'margin-bottom:10px;font-size:13px;line-height:1.6;">'
                '<b>Blok turlari:</b><br>'
                '<b>Matn bloki</b> — sarlavha + matn (HTML qo\'llab-quvvatlanadi).<br>'
                '<b>Rasm + Matn</b> — bir tomonda rasm, ikkinchi tomonda matn.<br>'
                '<b>Kartochkalar</b> — pastdagi «Kartochkalar» bo\'limida kartochkalar qo\'shing.<br>'
                '<b>Chaqiruv (CTA)</b> — diqqatni tortuvchi sarlavha + tugma havolasi.<br>'
                '<b>Bo\'luvchi chiziq</b> — bloklarni vizual ajratish uchun.'
                '</div>'
            ),
            'fields': ('page', 'block_type', 'order', 'is_active'),
        }),
        ("Sarlavha", {
            'fields': ('title_uz', 'title_kr', 'title_ru'),
        }),
        ("Matn", {
            'description': mark_safe(
                '<p class="help">HTML teglarini ishlatish mumkin. Misol: '
                '<code>&lt;b&gt;qalin&lt;/b&gt;</code>, '
                '<code>&lt;br&gt;</code> — yangi qator, '
                '<code>&lt;ul&gt;&lt;li&gt;...&lt;/li&gt;&lt;/ul&gt;</code> — ro\'yxat.</p>'
            ),
            'fields': ('content_uz', 'content_kr', 'content_ru'),
        }),
        ("Rasm (Rasm + Matn bloki uchun)", {
            'classes': ('collapse',),
            'fields': ('image', 'image_position'),
        }),
        ("Tugma / Havola (CTA uchun)", {
            'classes': ('collapse',),
            'fields': ('link_text_uz', 'link_text_kr', 'link_text_ru', 'link_url'),
        }),
    )

    def page_link(self, obj):
        url = reverse('admin:core_custompage_change', args=[obj.page_id])
        return format_html(
            '<a href="{}">{}</a>', url, obj.page.title_uz
        )
    page_link.short_description = "Sahifa"
