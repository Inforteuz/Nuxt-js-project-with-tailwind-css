from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import (
    GeneralInfo, SiteSettings, Banner, NavItem,
    FooterLink, PageSection, SectionCard, MediaAsset
)


# --- Oddiy admin uchun User/Group ni yashirish ---
class CMSAdminSite(admin.AdminSite):
    pass


# Unregister default User/Group, re-register only for superusers
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')

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


# --- Sayt sozlamalari ---
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'primary_color', 'secondary_color')

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


# --- Umumiy ma'lumot ---
@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'phone', 'email')
    fieldsets = (
        ("Tashkilot nomi", {'fields': ('name_uz', 'name_ru')}),
        ("Aloqa", {'fields': ('address_uz', 'address_ru', 'phone', 'hotline', 'email')}),
        ("Ish vaqti", {'fields': ('work_hours_uz', 'work_hours_ru')}),
        ("Ijtimoiy tarmoqlar", {'fields': ('telegram', 'facebook', 'instagram', 'youtube')}),
    )

    def has_add_permission(self, request):
        return not GeneralInfo.objects.exists()


# --- Bannerlar ---
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    fieldsets = (
        ("Sarlavha", {'fields': ('title_uz', 'title_ru', 'subtitle_uz', 'subtitle_ru')}),
        ("Tavsif", {'fields': ('description_uz', 'description_ru')}),
        ("Rasm va havola", {'fields': ('image', 'link')}),
        ("Sozlamalar", {'fields': ('order', 'is_active')}),
    )


# --- Navigatsiya ---
@admin.register(NavItem)
class NavItemAdmin(admin.ModelAdmin):
    list_display = ('label_uz', 'url', 'order', 'is_active')
    list_editable = ('order', 'is_active')


# --- Footer havolalar ---
@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ('label_uz', 'column', 'url', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('column',)


# --- Sahifa bo'limlari ---
class SectionCardInline(admin.StackedInline):
    model = SectionCard
    extra = 1
    fieldsets = (
        (None, {'fields': ('title_uz', 'title_ru', 'text_uz', 'text_ru', 'icon', 'image', 'link', 'order')}),
    )


@admin.register(PageSection)
class PageSectionAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'page', 'section_type', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('page', 'section_type')
    inlines = [SectionCardInline]
    fieldsets = (
        ("Asosiy", {'fields': ('page', 'section_type', 'order', 'is_active')}),
        ("Sarlavha", {'fields': ('title_uz', 'title_ru')}),
        ("Matn", {'fields': ('content_uz', 'content_ru')}),
        ("Rasm", {'fields': ('image',)}),
        ("Qo'shimcha (JSON)", {'fields': ('extra_data',), 'classes': ('collapse',)}),
    )


# --- Sayt rasmlari ---
@admin.register(MediaAsset)
class MediaAssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'image')
    list_filter = ('location',)
