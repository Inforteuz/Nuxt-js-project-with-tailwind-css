from rest_framework import viewsets, generics
from .models import GeneralInfo, Banner
from .serializers import GeneralInfoSerializer, BannerSerializer

class GeneralInfoView(generics.RetrieveAPIView):
    queryset = GeneralInfo.objects.all()
    serializer_class = GeneralInfoSerializer
    
    def get_object(self):
        return GeneralInfo.objects.first() or GeneralInfo()

class BannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Banner.objects.filter(is_active=True)
    serializer_class = BannerSerializer
