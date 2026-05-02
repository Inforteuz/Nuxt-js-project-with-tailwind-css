from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GeneralInfoView, BannerViewSet

router = DefaultRouter()
router.register(r"banners", BannerViewSet)

urlpatterns = [
    path("info/", GeneralInfoView.as_view()),
    path("", include(router.urls)),
]
