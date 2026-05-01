from django.contrib import admin
from .models import Category, News

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'slug')
    prepopulated_fields = {'slug': ('name_uz',)}

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'category', 'published_at', 'views_count', 'is_published')
    list_filter = ('is_published', 'category', 'published_at')
    search_fields = ('title_uz', 'content_uz')
    prepopulated_fields = {'slug': ('title_uz',)}
