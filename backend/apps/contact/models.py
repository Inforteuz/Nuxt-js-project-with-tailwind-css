from django.db import models

class Appeal(models.Model):
    STATUS_CHOICES = (
        ('new', 'Yangi'),
        ('in_progress', "Ko'rib chiqilmoqda"),
        ('resolved', "Hal etildi"),
        ('rejected', "Rad etildi"),
    )
    
    full_name = models.CharField(max_length=255, verbose_name="F.I.Sh.")
    phone = models.CharField(max_length=50, verbose_name="Telefon raqami")
    email = models.EmailField(verbose_name="Elektron pochta", blank=True)
    subject = models.CharField(max_length=255, verbose_name="Murojaat mavzusi")
    message = models.TextField(verbose_name="Murojaat matni")
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Holati")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan vaqti")
    
    class Meta:
        verbose_name = "Murojaat"
        verbose_name_plural = "Murojaatlar"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.subject}"
