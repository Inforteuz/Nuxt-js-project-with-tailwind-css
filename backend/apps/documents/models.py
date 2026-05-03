from django.db import models

class DocumentCategory(models.Model):
    name_uz = models.CharField(max_length=100, verbose_name="Kategoriya nomi (O'z)")
    name_kr = models.CharField(max_length=100, blank=True, verbose_name="Kategoriya nomi (Kr)")
    name_ru = models.CharField(max_length=100, verbose_name="Kategoriya nomi (Ru)", blank=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Hujjat kategoriyasi"
        verbose_name_plural = "Hujjat kategoriyalari"

    def __str__(self):
        return self.name_uz

class Document(models.Model):
    category = models.ForeignKey(DocumentCategory, on_delete=models.SET_NULL, null=True, related_name='documents', verbose_name="Kategoriya")
    title_uz = models.CharField(max_length=255, verbose_name="Sarlavha (O'z)")
    title_kr = models.CharField(max_length=255, blank=True, verbose_name="Sarlavha (Kr)")
    title_ru = models.CharField(max_length=255, verbose_name="Sarlavha (Ru)", blank=True)
    
    number = models.CharField(max_length=50, verbose_name="Hujjat raqami", blank=True)
    date = models.DateField(verbose_name="Qabul qilingan sana")
    
    file = models.FileField(upload_to='documents/', verbose_name="Fayl", blank=True, null=True)
    link = models.URLField(verbose_name="Tashqi havola", blank=True)
    
    is_active = models.BooleanField(default=True, verbose_name="Faol")

    class Meta:
        verbose_name = "Hujjat"
        verbose_name_plural = "Hujjatlar"
        ordering = ['-date']

    def __str__(self):
        return self.title_uz
