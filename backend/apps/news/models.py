from django.db import models

class Category(models.Model):
    name_uz = models.CharField(max_length=100, verbose_name="Kategoriya nomi (O'z)")
    name_kr = models.CharField(max_length=100, blank=True, verbose_name="Kategoriya nomi (Kr)")
    name_ru = models.CharField(max_length=100, verbose_name="Kategoriya nomi (Ru)", blank=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return self.name_uz

class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='news', verbose_name="Kategoriya")
    title_uz = models.CharField(max_length=255, verbose_name="Sarlavha (O'z)")
    title_kr = models.CharField(max_length=255, blank=True, verbose_name="Sarlavha (Kr)")
    title_ru = models.CharField(max_length=255, verbose_name="Sarlavha (Ru)", blank=True)
    slug = models.SlugField(unique=True)
    
    image = models.ImageField(upload_to='news_images/', verbose_name="Rasm", blank=True, null=True)
    
    content_uz = models.TextField(verbose_name="Matn (O'z)")
    content_kr = models.TextField(blank=True, verbose_name="Matn (Kr)")
    content_ru = models.TextField(verbose_name="Matn (Ru)", blank=True)
    
    views_count = models.PositiveIntegerField(default=0, verbose_name="Ko'rishlar soni")
    is_published = models.BooleanField(default=True, verbose_name="Chop etilgan")
    
    published_at = models.DateTimeField(verbose_name="Chop etilgan sana")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
        ordering = ['-published_at']

    def __str__(self):
        return self.title_uz
