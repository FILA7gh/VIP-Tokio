from django.urls import path
from . import views


urlpatterns = [
    path('basicservice/', views.BasicServiceAPIView.as_view(), name='basicservice'),
]

