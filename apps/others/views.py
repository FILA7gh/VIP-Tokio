from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import *
from rest_framework import permissions


class SupportAPIView(CreateAPIView):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer


class MiniBlogAPIView(ListCreateAPIView):
    queryset = MiniBlog.objects.all()
    serializer_class = MiniBlogSerializer


class MiniBlogDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = MiniBlog.objects.all()
    serializer_class = MiniBlogSerializer
    permission_classes = [IsOwnerOrReadOnly, ]


class AboutUsAPIView(ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAdminOrReadOnly, ]


class AboutUsDetailAPIView(ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAdminOrReadOnly, ]




