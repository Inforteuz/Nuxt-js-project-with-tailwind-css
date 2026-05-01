from django.contrib import admin
from .models import Appeal

@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'subject', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('full_name', 'phone', 'subject', 'message')
    readonly_fields = ('full_name', 'phone', 'email', 'subject', 'message', 'created_at')
