from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('reset/login/<int:pk>', views.ResetLoginAPIView.as_view()),
    path('reset/password/<int:pk>', views.ResetPassword.as_view()),

]
