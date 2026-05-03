from rest_framework import serializers
from .models import Appeal

class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = ['full_name', 'phone', 'email', 'region', 'subject', 'message']
        extra_kwargs = {
            'email': {'required': False, 'allow_blank': True},
            'region': {'required': False, 'allow_blank': True},
        }
