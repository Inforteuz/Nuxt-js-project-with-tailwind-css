from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GeneralInfoView, SiteSettingsView, BannerViewSet,
    NavItemViewSet, FooterLinkViewSet, PageSectionViewSet,
    MediaAssetViewSet,
    CustomPageListView, CustomPageDetailView,
)

router = DefaultRouter()
router.register(r"banners", BannerViewSet)
router.register(r"nav", NavItemViewSet)
router.register(r"footer-links", FooterLinkViewSet)
router.register(r"sections", PageSectionViewSet, basename="section")
router.register(r"media", MediaAssetViewSet)

urlpatterns = [
    path("info/", GeneralInfoView.as_view()),
    path("site-settings/", SiteSettingsView.as_view()),
    path("pages/", CustomPageListView.as_view()),
    path("pages/<slug:slug>/", CustomPageDetailView.as_view()),
    path("", include(router.urls)),
]
