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
# Sayt sozlamalari (ranglar, logo)
# ============================================================
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'primary_color_preview', 'secondary_color_preview', 'accent_color_preview')

    fieldsets = (
        ("Ranglar", {
            'description': "Sayt ranglarini bu yerda o'zgartiring. Hex format: #RRGGBB (masalan: #0A4D8C)",
            'fields': ('primary_color', 'secondary_color', 'accent_color'),
        }),
        ("Logotip va Favicon", {
            'fields': ('logo', 'favicon'),
        }),
    )

    def primary_color_preview(self, obj):
        return format_html(
            '<span style="display:inline-block;width:20px;height:20px;background:{};border-radius:4px;border:1px solid #ddd;vertical-align:middle;margin-right:6px;"></span>{}',
            obj.primary_color, obj.primary_color
        )
    primary_color_preview.short_description = "Asosiy rang"

    def secondary_color_preview(self, obj):
        return format_html(
            '<span style="display:inline-block;width:20px;height:20px;background:{};border-radius:4px;border:1px solid #ddd;vertical-align:middle;margin-right:6px;"></span>{}',
            obj.secondary_color, obj.secondary_color
        )
    secondary_color_preview.short_description = "Ikkinchi rang"

    def accent_color_preview(self, obj):
        return format_html(
            '<span style="display:inline-block;width:20px;height:20px;background:{};border-radius:4px;border:1px solid #ddd;vertical-align:middle;margin-right:6px;"></span>{}',
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
        ("Tashkilot nomi", {
            'fields': ('name_uz', 'name_kr', 'name_ru'),
        }),
        ("Aloqa ma'lumotlari", {
            'fields': ('address_uz', 'address_kr', 'address_ru', 'phone', 'hotline', 'email'),
        }),
        ("Ish vaqti", {
            'fields': ('work_hours_uz', 'work_hours_kr', 'work_hours_ru'),
        }),
        ("Boshqarma haqida", {
            'fields': ('about_uz', 'about_kr', 'about_ru'),
        }),
        ("Boshqarma tarixi", {
            'classes': ('collapse',),
            'fields': ('history_uz', 'history_kr', 'history_ru'),
        }),
        ("Nizom", {
            'fields': ('statute_link',),
        }),
        ("Ijtimoiy tarmoqlar", {
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

    fieldsets = (
        ("Sarlavha", {'fields': ('title_uz', 'title_kr', 'title_ru')}),
        ("Qo'shimcha sarlavha", {'fields': ('subtitle_uz', 'subtitle_kr', 'subtitle_ru')}),
        ("Tavsif", {'fields': ('description_uz', 'description_kr', 'description_ru')}),
        ("Rasm va havola", {'fields': ('image', 'link')}),
        ("Sozlamalar", {'fields': ('order', 'is_active')}),
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


# ============================================================
# Footer havolalar
# ============================================================
@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ('label_uz', 'column', 'url', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('column',)
    fields = ('column', 'label_uz', 'label_kr', 'label_ru', 'url', 'is_external', 'order', 'is_active')


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

    fieldsets = (
        ("Asosiy sozlamalar", {'fields': ('page', 'section_type', 'order', 'is_active')}),
        ("Sarlavha", {'fields': ('title_uz', 'title_kr', 'title_ru')}),
        ("Matn", {'fields': ('content_uz', 'content_kr', 'content_ru')}),
        ("Rasm", {'fields': ('image',)}),
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

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px;border-radius:6px;"/>', obj.image.url)
        return "—"
    image_preview.short_description = "Ko'rinish"
