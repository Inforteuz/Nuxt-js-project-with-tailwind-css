from django.db import models

class GeneralInfo(models.Model):
    name_uz = models.CharField(max_length=255, verbose_name="Tashkilot nomi (O'z)")
    name_ru = models.CharField(max_length=255, verbose_name="Tashkilot nomi (Ru)", blank=True)
    address = models.TextField(verbose_name="Manzil")
    phone = models.CharField(max_length=50, verbose_name="Telefon raqami")
    hotline = models.CharField(max_length=50, verbose_name="Ishonch telefoni", blank=True)
    email = models.EmailField(verbose_name="Elektron pochta", blank=True)
    work_hours = models.CharField(max_length=255, verbose_name="Ish vaqti", blank=True)
    
    # Ijtimoiy tarmoqlar
    telegram = models.URLField(blank=True, verbose_name="Telegram havolasi")
    facebook = models.URLField(blank=True, verbose_name="Facebook havolasi")
    instagram = models.URLField(blank=True, verbose_name="Instagram havolasi")
    youtube = models.URLField(blank=True, verbose_name="YouTube havolasi")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Umumiy ma'lumot"
        verbose_name_plural = "Umumiy ma'lumotlar"

    def __str__(self):
        return self.name_uz

