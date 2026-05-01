from rest_framework import generics
from .models import News
from .serializers import NewsListSerializer, NewsDetailSerializer

class NewsListView(generics.ListAPIView):
    queryset = News.objects.filter(is_published=True)
    serializer_class = NewsListSerializer

class NewsDetailView(generics.RetrieveAPIView):
    queryset = News.objects.filter(is_published=True)
    serializer_class = NewsDetailSerializer
    lookup_field = 'id'

    def get_object(self):
        obj = super().get_object()
        # Increment views count
        obj.views_count += 1
        obj.save(update_fields=['views_count'])
        return obj
