from rest_framework import serializers
from .models import News, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name_uz', 'name_ru', 'slug']

class NewsListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = News
        fields = ['id', 'title_uz', 'title_ru', 'slug', 'image', 'category', 'published_at', 'views_count']

class NewsDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = News
        fields = '__all__'
