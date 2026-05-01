from django.contrib import admin
from .models import DocumentCategory, Document

@admin.register(DocumentCategory)
class DocumentCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'slug')
    prepopulated_fields = {'slug': ('name_uz',)}

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'category', 'date', 'is_active')
    list_filter = ('is_active', 'category', 'date')
    search_fields = ('title_uz', 'number')
