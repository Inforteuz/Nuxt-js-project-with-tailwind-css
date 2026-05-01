from rest_framework import generics
from .models import Appeal
from .serializers import AppealSerializer

class AppealCreateView(generics.CreateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer
