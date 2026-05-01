from django.db import models

class Department(models.Model):
    name_uz = models.CharField(max_length=255, verbose_name="Bo'lim/Boshqarma nomi (O'z)")
    name_ru = models.CharField(max_length=255, verbose_name="Bo'lim/Boshqarma nomi (Ru)", blank=True)
    description_uz = models.TextField(verbose_name="Tavsifi (O'z)", blank=True)
    description_ru = models.TextField(verbose_name="Tavsifi (Ru)", blank=True)
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")

    class Meta:
        verbose_name = "Tuzilma bo'limi"
        verbose_name_plural = "Tashkiliy tuzilma"
        ordering = ['order']

    def __str__(self):
        return self.name_uz
