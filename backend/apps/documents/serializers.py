from rest_framework import serializers
from .models import Document, DocumentCategory

class DocumentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentCategory
        fields = ['id', 'name_uz', 'name_ru', 'slug']

class DocumentSerializer(serializers.ModelSerializer):
    category = DocumentCategorySerializer()
    
    class Meta:
        model = Document
        fields = '__all__'
