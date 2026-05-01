from rest_framework import generics
from .models import Leader
from .serializers import LeaderSerializer

class LeaderListView(generics.ListAPIView):
    queryset = Leader.objects.filter(is_active=True)
    serializer_class = LeaderSerializer
