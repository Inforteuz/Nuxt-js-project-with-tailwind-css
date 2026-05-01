from django.contrib import admin
from .models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'order')
    list_editable = ('order',)
    search_fields = ('name_uz', 'description_uz')
