from rest_framework import generics
from .models import Document
from .serializers import DocumentSerializer

class DocumentListView(generics.ListAPIView):
    queryset = Document.objects.filter(is_active=True)
    serializer_class = DocumentSerializer
