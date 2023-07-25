from django.urls import path
from . import views


urlpatterns = [
    path('', views.ModelAPIView.as_view()),
    path('<int:pk>/', views.ModelDetailAPIView.as_view()),

    path('<int:model_id>/reviews/', views.ReviewAPIView.as_view()),

]
