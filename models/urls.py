from django.urls import path
from . import views


urlpatterns = [
    path('', views.ModelApiView.as_view()),
    path('<int:id_>/', views.ModelDetailApiView.as_view()),
]
