from django.db import models

class Position(models.Model):
    name_uz = models.CharField(max_length=200, verbose_name="Lavozim nomi (O'z)")
    name_kr = models.CharField(max_length=200, blank=True, verbose_name="Lavozim nomi (Kr)")
    name_ru = models.CharField(max_length=200, verbose_name="Lavozim nomi (Ru)", blank=True)
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")

    class Meta:
        verbose_name = "Lavozim"
        verbose_name_plural = "Lavozimlar"
        ordering = ['order']

    def __str__(self):
        return self.name_uz

class Leader(models.Model):
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, verbose_name="Lavozimi")
    full_name_uz = models.CharField(max_length=200, verbose_name="F.I.Sh. (O'z)")
    full_name_kr = models.CharField(max_length=200, blank=True, verbose_name="F.I.Sh. (Kr)")
    full_name_ru = models.CharField(max_length=200, verbose_name="F.I.Sh. (Ru)", blank=True)
    
    image = models.ImageField(upload_to='leaders/', verbose_name="Rasm", blank=True, null=True)
    
    phone = models.CharField(max_length=50, verbose_name="Telefon raqami", blank=True)
    email = models.EmailField(verbose_name="Elektron pochta", blank=True)
    reception_days_uz = models.CharField(max_length=255, verbose_name="Qabul kunlari (O'z)", blank=True)
    reception_days_kr = models.CharField(max_length=255, verbose_name="Qabul kunlari (Kr)", blank=True)
    reception_days_ru = models.CharField(max_length=255, verbose_name="Qabul kunlari (Ru)", blank=True)
    
    biography_uz = models.TextField(verbose_name="Biografiya (O'z)", blank=True)
    biography_kr = models.TextField(verbose_name="Biografiya (Kr)", blank=True)
    biography_ru = models.TextField(verbose_name="Biografiya (Ru)", blank=True)
    
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    is_active = models.BooleanField(default=True, verbose_name="Faol")

    class Meta:
        verbose_name = "Rahbar"
        verbose_name_plural = "Rahbariyat"
        ordering = ['order', 'position__order']

    def __str__(self):
        return self.full_name_uz
