from django.contrib import admin
from .models import Position, Leader

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'order')
    list_editable = ('order',)

@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ('full_name_uz', 'position', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active', 'position')
    search_fields = ('full_name_uz', 'phone', 'email')
