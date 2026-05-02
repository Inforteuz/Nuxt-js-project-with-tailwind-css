from rest_framework import serializers
from .models import Position, Leader

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name_uz', 'name_kr', 'name_ru']

class LeaderSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    
    class Meta:
        model = Leader
        fields = '__all__'
