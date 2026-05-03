from django.contrib import admin
from .models import Appeal


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'region', 'subject', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'region')
    search_fields = ('full_name', 'phone', 'subject', 'message', 'region')
    readonly_fields = ('full_name', 'phone', 'email', 'region', 'subject', 'message', 'created_at')
    list_per_page = 25
    date_hierarchy = 'created_at'

    fieldsets = (
        ("Foydalanuvchi ma'lumotlari", {'fields': ('full_name', 'phone', 'email', 'region')}),
        ("Murojaat matni", {'fields': ('subject', 'message', 'created_at')}),
        ("Ko'rib chiqish holati", {'fields': ('status',)}),
    )

    def has_add_permission(self, request):
        return False
