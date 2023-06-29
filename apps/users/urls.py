from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('reset/login/', views.ResetLoginAPIView.as_view()),
    path('reset/password/', views.ResetPasswordAPIView.as_view()),
    path('reset/password/confirm/', views.ResetConfirmPasswordAPIView.as_view()),
    path('password/change/<str:username>/', views.ChangePasswordAPIView.as_view()),

]
