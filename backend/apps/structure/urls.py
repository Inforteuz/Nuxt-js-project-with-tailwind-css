from django.urls import path
from .views import DepartmentListView

urlpatterns = [
    path('structure/', DepartmentListView.as_view(), name='structure-list'),
]
