from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from .models import (
    GeneralInfo, SiteSettings, Banner, NavItem,
    FooterLink, PageSection, MediaAsset,
    CustomPage,
)
from .serializers import (
    GeneralInfoSerializer, SiteSettingsSerializer, BannerSerializer,
    NavItemSerializer, FooterLinkSerializer, PageSectionSerializer,
    MediaAssetSerializer,
    CustomPageSerializer, CustomPageListSerializer,
)


class GeneralInfoView(APIView):
    def get(self, request):
        obj = GeneralInfo.objects.first()
        if obj:
            serializer = GeneralInfoSerializer(obj, context={'request': request})
            return Response(serializer.data)
        return Response({})


class SiteSettingsView(APIView):
    def get(self, request):
        obj = SiteSettings.objects.first()
        if obj:
            serializer = SiteSettingsSerializer(obj, context={'request': request})
            return Response(serializer.data)
        return Response({
            'primary_color': '#0ea5e9',
            'secondary_color': '#14b8a6',
            'accent_color': '#f59e0b',
        })


class BannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Banner.objects.filter(is_active=True)
    serializer_class = BannerSerializer


class NavItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NavItem.objects.filter(is_active=True)
    serializer_class = NavItemSerializer


class FooterLinkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FooterLink.objects.filter(is_active=True)
    serializer_class = FooterLinkSerializer


class PageSectionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PageSectionSerializer

    def get_queryset(self):
        qs = PageSection.objects.filter(is_active=True)
        page = self.request.query_params.get('page')
        if page:
            qs = qs.filter(page=page)
        return qs


class MediaAssetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MediaAsset.objects.all()
    serializer_class = MediaAssetSerializer

    def get_queryset(self):
        qs = MediaAsset.objects.all()
        location = self.request.query_params.get('location')
        if location:
            qs = qs.filter(location=location)
        return qs


class CustomPageListView(generics.ListAPIView):
    """GET /api/v1/pages/ — all active pages (for nav or sitemap)."""
    serializer_class = CustomPageListSerializer

    def get_queryset(self):
        return CustomPage.objects.filter(is_active=True)


class CustomPageDetailView(generics.RetrieveAPIView):
    """GET /api/v1/pages/<slug>/ — full page with all blocks."""
    serializer_class = CustomPageSerializer
    lookup_field = 'slug'

    def get_object(self):
        slug = self.kwargs['slug']
        try:
            return CustomPage.objects.get(slug=slug, is_active=True)
        except CustomPage.DoesNotExist:
            raise NotFound(detail=f"'{slug}' sahifasi topilmadi yoki faol emas.")
