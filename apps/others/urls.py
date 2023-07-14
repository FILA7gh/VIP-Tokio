from django.urls import path
from . import views


urlpatterns = [
    path('support/', views.SupportAPIView.as_view()),

    path('miniblog/', views.MiniBlogViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('miniblog/<int:pk>/', views.MiniBlogViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('about-us/', views.AboutUsAPIView.as_view()),
    path('help/', views.HelpAPIView.as_view()),
    path('didyouknow/', views.DidYouKnowAPIView.as_view()),
    path('rules/', views.RulesAPIView.as_view()),
]
