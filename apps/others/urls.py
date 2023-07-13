from django.urls import path
from . import views


urlpatterns = [
    # path('support/', SupportAPIView.as_view(), name="support"),
    # path('miniblog/', MiniBlogAPIView.as_view(), name="miniblog"),
    # path('miniblog/<int:pk>/', MiniBlogDetailAPIView.as_view(), name="miniblogdetail"),
    path('about-us/', views.AboutUsAPIView.as_view()),
    path('help/', views.HelpAPIView.as_view()),
    path('didyouknow/', views.DidYouKnowAPIView.as_view()),
]


