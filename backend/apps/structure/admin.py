from django.contrib import admin
from .models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'head_name_uz', 'order')
    list_editable = ('order',)
    search_fields = ('name_uz', 'description_uz', 'head_name_uz')

    fieldsets = (
        ("Bo'lim nomi", {
            'fields': ('name_uz', 'name_kr', 'name_ru'),
        }),
        ("Tavsif", {
            'fields': ('description_uz', 'description_kr', 'description_ru'),
        }),
        ("Bo'lim boshlig'i", {
            'fields': ('head_name_uz', 'head_name_kr', 'head_name_ru'),
        }),
        ("Tartib", {
            'fields': ('order',),
        }),
    )
