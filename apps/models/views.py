from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status, permissions

from .permissions import IsAdminOrAuthorOrReadOnly
from .models import Model, Review
from .serializers import ModelSerializer, ModelDetailSerializer, ModelValidateSerializer, ReviewSerializer


class ModelAPIView(ListCreateAPIView):
    queryset = Model.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminOrAuthorOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ModelSerializer
        elif self.request.method == 'POST':
            return ModelDetailSerializer

    def post(self, request, *args, **kwargs):
        serializer = ModelValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        model = serializer.save()
        response_serializer = ModelSerializer(model, context={'request': request})
        return Response(data=response_serializer.data)


class ModelDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelDetailSerializer
    permission_classes = [IsAdminOrAuthorOrReadOnly]

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ModelValidateSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_serializer = ModelDetailSerializer(instance, context={'request': request})
        return Response(data=response_serializer.data, status=status.HTTP_200_OK)


class ReviewAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        model_id = self.kwargs['model_id']
        return Review.objects.filter(model_id=model_id)
