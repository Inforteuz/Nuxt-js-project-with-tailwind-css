from django import forms
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.html import format_html, mark_safe
from .models import (
    GeneralInfo, SiteSettings, Banner, NavItem,
    FooterLink, PageSection, SectionCard, MediaAsset
)

admin.site.site_header = "Andijon SSB — Boshqaruv paneli"
admin.site.site_title = "Andijon SSB Admin"
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
