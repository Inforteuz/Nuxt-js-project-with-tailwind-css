from django import forms
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.html import format_html
from .models import (
    GeneralInfo, SiteSettings, Banner, NavItem,
    FooterLink, PageSection, SectionCard, MediaAsset
)

# ============================================================
# Admin sayt sarlavhasi
# ============================================================
admin.site.site_header = "Andijon SSB — Boshqaruv paneli"
admin.site.site_title = "Andijon SSB Admin"
admin.site.index_title = "Saytni boshqarish"


# ============================================================
# Foydalanuvchilar — faqat superadmin ko'ra oladi
# ============================================================
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


# ============================================================
# Color picker widget
# ============================================================
class ColorPickerWidget(forms.TextInput):
    """HTML5 color picker — vizual rang tanlash."""
    input_type = 'color'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs.update({
            'style': 'width:70px; height:42px; padding:2px 4px; cursor:pointer; border-radius:6px;'
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


# ============================================================
# Sayt sozlamalari (ranglar, logo)
# ============================================================
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    form = SiteSettingsForm
    list_display = ('__str__', 'primary_color_preview', 'secondary_color_preview', 'accent_color_preview')

    fieldsets = (
        ("🎨 Sayt ranglari", {
            'description': (
                "<div style='background:#fff3cd;border:1px solid #ffc107;border-radius:8px;"
                "padding:14px 18px;margin-bottom:12px;font-size:14px;line-height:1.7;'>"
                "<b>📌 Bu bo'lim saytning BARCHA ranglarini boshqaradi:</b><br>"
                "• <b>Asosiy rang</b> — navbar, tugmalar, sarlavhalar rangi (odatda ko'k)<br>"
                "• <b>Ikkinchi rang</b> — kategoriya belgilari, hover effektlar (odatda yashil)<br>"
                "• <b>Aksent rang</b> — e'lon, badge, muhim elementlar (odatda sariq/to'q sariq)<br>"
                "<br>Rangni tanlash uchun kvadrat tugmani bosing → vizual rang palitrasidan tanlang → <b>Saqlash</b>."
                "</div>"
            ),
            'fields': ('primary_color', 'secondary_color', 'accent_color'),
        }),
        ("🖼️ Logotip va Favicon", {
            'description': (
                "<div style='background:#e8f4fd;border:1px solid #bee3f8;border-radius:8px;"
                "padding:12px 16px;margin-bottom:10px;font-size:13px;line-height:1.6;'>"
                "• <b>Logotip</b> — navbar yuqori chap burchagida ko'rinadi (PNG, SVG tavsiya etiladi)<br>"
                "• <b>Favicon</b> — brauzer tab ikonkasi (32×32 px, ICO yoki PNG)"
                "</div>"
            ),
            'fields': ('logo', 'favicon'),
        }),
    )

    def primary_color_preview(self, obj):
        return format_html(
            '<span style="display:inline-block;width:24px;height:24px;background:{};'
            'border-radius:50%;border:2px solid #ddd;vertical-align:middle;margin-right:6px;"></span>'
            '<code style="font-size:12px;">{}</code>',
            obj.primary_color, obj.primary_color
        )
    primary_color_preview.short_description = "Asosiy rang"

    def secondary_color_preview(self, obj):
        return format_html(
            '<span style="display:inline-block;width:24px;height:24px;background:{};'
            'border-radius:50%;border:2px solid #ddd;vertical-align:middle;margin-right:6px;"></span>'
            '<code style="font-size:12px;">{}</code>',
            obj.secondary_color, obj.secondary_color
        )
    secondary_color_preview.short_description = "Ikkinchi rang"

    def accent_color_preview(self, obj):
        return format_html(
            '<span style="display:inline-block;width:24px;height:24px;background:{};'
            'border-radius:50%;border:2px solid #ddd;vertical-align:middle;margin-right:6px;"></span>'
            '<code style="font-size:12px;">{}</code>',
            obj.accent_color, obj.accent_color
        )
    accent_color_preview.short_description = "Aksent rang"

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


# ============================================================
# Umumiy ma'lumot
# ============================================================
@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'phone', 'email')

    fieldsets = (
        ("🏛️ Tashkilot nomi", {
            'description': (
                "<div style='background:#e8f4fd;border:1px solid #bee3f8;border-radius:8px;"
                "padding:12px 16px;margin-bottom:10px;font-size:13px;'>"
                "Saytning barcha joyida ko'rinadigan rasmiy tashkilot nomi. "
                "Navbar, footer va brauzer tab sarlavhasida ishlatiladi."
                "</div>"
            ),
            'fields': ('name_uz', 'name_kr', 'name_ru'),
        }),
        ("📞 Aloqa ma'lumotlari", {
            'description': (
                "<div style='background:#e8f4fd;border:1px solid #bee3f8;border-radius:8px;"
                "padding:12px 16px;margin-bottom:10px;font-size:13px;'>"
                "Header yuqorisidagi kontakt satr va <b>Aloqa</b> sahifasida ko'rinadi."
                "</div>"
            ),
            'fields': ('address_uz', 'address_kr', 'address_ru', 'phone', 'hotline', 'email'),
        }),
        ("🕐 Ish vaqti", {
            'description': (
                "<div style='background:#e8f4fd;border:1px solid #bee3f8;border-radius:8px;"
                "padding:12px 16px;margin-bottom:10px;font-size:13px;'>"
                "Aloqa sahifasi va footer'da ko'rinadigan qabul vaqtlari."
                "</div>"
            ),
            'fields': ('work_hours_uz', 'work_hours_kr', 'work_hours_ru'),
        }),
        ("📝 Boshqarma haqida", {
            'description': (
                "<div style='background:#e8f4fd;border:1px solid #bee3f8;border-radius:8px;"
                "padding:12px 16px;margin-bottom:10px;font-size:13px;'>"
                "<b>«Biz haqimizda»</b> sahifasining asosiy matni — tashkilot faoliyati tavsifi."
                "</div>"
            ),
            'fields': ('about_uz', 'about_kr', 'about_ru'),
        }),
        ("📜 Boshqarma tarixi", {
            'classes': ('collapse',),
            'description': (
                "<div style='background:#e8f4fd;border:1px solid #bee3f8;border-radius:8px;"
                "padding:12px 16px;margin-bottom:10px;font-size:13px;'>"
                "«Biz haqimizda» sahifasidagi «Tarix» bo'limida ko'rinadi."
                "</div>"
            ),
            'fields': ('history_uz', 'history_kr', 'history_ru'),
        }),
        ("📄 Nizom", {
            'description': (
                "<div style='background:#e8f4fd;border:1px solid #bee3f8;border-radius:8px;"
                "padding:12px 16px;margin-bottom:10px;font-size:13px;'>"
                "Tashkilot nizomi PDF havolasi — «Biz haqimizda» sahifasidagi «Nizomni yuklab olish» tugmasi."
                "</div>"
            ),
            'fields': ('statute_link',),
        }),
        ("🌐 Ijtimoiy tarmoqlar", {
            'description': (
                "<div style='background:#e8f4fd;border:1px solid #bee3f8;border-radius:8px;"
                "padding:12px 16px;margin-bottom:10px;font-size:13px;'>"
                "Footer pastki qismidagi ijtimoiy tarmoq ikonkalari va havolalari."
                "</div>"
            ),
            'fields': ('telegram', 'facebook', 'instagram', 'youtube'),
        }),
    )

    def has_add_permission(self, request):
        return not GeneralInfo.objects.exists()


# ============================================================
# Bannerlar (karusel)
# ============================================================
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'image_preview', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_display_links = ('title_uz',)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['subtitle'] = (
            "Bu yerda bosh sahifadagi karusel (slayder) bannerlarini boshqarasiz. "
            "«Faol» belgisi qo'yilgan bannerlar saytda ko'rinadi. "
            "Tartib raqamini o'zgartirib bannerlar ketma-ketligini sozlang."
        )
        return super().changelist_view(request, extra_context=extra_context)

    fieldsets = (
        ("ℹ️ Sarlavha matni", {
            'description': (
                "<div style='background:#fff3cd;border:1px solid #ffc107;border-radius:8px;"
                "padding:12px 16px;margin-bottom:10px;font-size:13px;'>"
                "📍 <b>Bosh sahifadagi karusel banneri.</b> Sarlavha bannerning markazida katta harflar bilan ko'rinadi."
                "</div>"
            ),
            'fields': ('title_uz', 'title_kr', 'title_ru'),
        }),
        ("Qo'shimcha sarlavha", {'fields': ('subtitle_uz', 'subtitle_kr', 'subtitle_ru')}),
        ("Tavsif matni", {
            'description': "<small style='color:#666;'>Sarlavha ostida kichik matn — qisqacha tavsif.</small>",
            'fields': ('description_uz', 'description_kr', 'description_ru'),
        }),
        ("🖼️ Rasm va havola", {
            'description': (
                "<small style='color:#666;'>Tavsiya etilgan rasm o'lchami: <b>1920×700 px</b>. "
                "Havola: masalan <code>/about</code> yoki <code>https://...</code></small>"
            ),
            'fields': ('image', 'link'),
        }),
        ("⚙️ Sozlamalar", {'fields': ('order', 'is_active')}),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:40px;border-radius:4px;"/>', obj.image.url)
        return "—"
    image_preview.short_description = "Rasm"


# ============================================================
# Navigatsiya (Navbar)
# ============================================================
@admin.register(NavItem)
class NavItemAdmin(admin.ModelAdmin):
    list_display = ('label_uz', 'url', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    fields = ('label_uz', 'label_kr', 'label_ru', 'url', 'order', 'is_active')

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['subtitle'] = (
            "Saytning yuqori navigatsiya menyusi (navbar). "
            "«Faol» belgisi qo'yilgan elementlar ko'rinadi. "
            "Havola: /news, /about, /contact kabi ichki yo'llar yoki https://... tashqi havolalar."
        )
        return super().changelist_view(request, extra_context=extra_context)


# ============================================================
# Footer havolalar
# ============================================================
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
            "«Tezkor havolalar» — ichki sahifalar (Yangiliklar, Hujjatlar va h.k.). "
            "«Davlat saytlari» — tashqi davlat portallari. "
            "«Tashqi havola» belgisi qo'yilsa yangi oynada ochiladi."
        )
        return super().changelist_view(request, extra_context=extra_context)


# ============================================================
# Sahifa bo'limlari (CMS sections)
# ============================================================
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

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['subtitle'] = (
            "Sayt sahifalaridagi dinamik bo'limlar. «Sahifa» maydoni qaysi sahifaga tegishli ekanini bildiradi "
            "(home = bosh sahifa, about = biz haqimizda va h.k.). "
            "«Kartochkalar» bo'lim turi tanlanganida quyidagi kartochkalarni qo'shing."
        )
        return super().changelist_view(request, extra_context=extra_context)

    fieldsets = (
        ("⚙️ Asosiy sozlamalar", {
            'description': (
                "<div style='background:#fff3cd;border:1px solid #ffc107;border-radius:8px;"
                "padding:12px 16px;margin-bottom:10px;font-size:13px;line-height:1.7;'>"
                "<b>Sahifa:</b> <code>home</code> = Bosh sahifa, <code>about</code> = Biz haqimizda<br>"
                "<b>Bo'lim turi:</b> Matn bloki / Kartochkalar / Statistika / Chaqiruv (CTA)<br>"
                "<b>Tartib raqami:</b> kichikroq raqam — yuqoriroq joylashadi"
                "</div>"
            ),
            'fields': ('page', 'section_type', 'order', 'is_active'),
        }),
        ("📝 Sarlavha", {'fields': ('title_uz', 'title_kr', 'title_ru')}),
        ("Matn", {'fields': ('content_uz', 'content_kr', 'content_ru')}),
        ("🖼️ Rasm", {'fields': ('image',)}),
        ("Qo'shimcha ma'lumot (JSON)", {'fields': ('extra_data',), 'classes': ('collapse',)}),
    )


# ============================================================
# Sayt rasmlari (MediaAsset)
# ============================================================
@admin.register(MediaAsset)
class MediaAssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'image_preview', 'alt_text')
    list_filter = ('location',)
    fields = ('name', 'location', 'image', 'alt_text')

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['subtitle'] = (
            "Saytning asosiy rasmlari. Joylashuvni tanlang: "
            "«Bosh sahifa fon rasmi» — hero section background; "
            "«Biz haqimizda rasm» — about sahifasi rasmi; "
            "«Aloqa sahifasi rasmi» — contact sahifasi rasmi."
        )
        return super().changelist_view(request, extra_context=extra_context)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px;border-radius:6px;"/>', obj.image.url)
        return "—"
    image_preview.short_description = "Ko'rinish"
