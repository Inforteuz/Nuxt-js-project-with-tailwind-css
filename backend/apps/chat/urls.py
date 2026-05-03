from django.urls import path
from .views import ChatView, ChatConfigView

urlpatterns = [
    path('chat/',        ChatView.as_view()),
    path('chat/config/', ChatConfigView.as_view()),
]
