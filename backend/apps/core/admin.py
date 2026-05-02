from django.contrib import admin
from .models import GeneralInfo

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ('name_uz', 'phone', 'email')

    def has_add_permission(self, request):
        if GeneralInfo.objects.exists():
            return False
        return True

from .models import Banner

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title_uz", "order", "is_active")
