from django.urls import path
from .views import AppealCreateView

urlpatterns = [
    path('contact/', AppealCreateView.as_view(), name='contact-create'),
]
