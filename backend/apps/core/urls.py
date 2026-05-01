from django.urls import path
from .views import GeneralInfoAPIView

urlpatterns = [
    path('info/', GeneralInfoAPIView.as_view(), name='general-info'),
]
