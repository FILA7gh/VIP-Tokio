from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser
from rest_framework import status

from .models import Model
from .serializers import ModelSerializer, ModelDetailSerializer, ModelValidateSerializer


class ModelAPIView(ListCreateAPIView):
    queryset = Model.objects.all()
    pagination_class = PageNumberPagination
    parser_classes = [MultiPartParser]
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ModelSerializer
        elif self.request.method == 'POST':
            return ModelDetailSerializer

    def post(self, request, *args, **kwargs):
        serializer = ModelValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=ModelSerializer(serializer, context={'request': request}).data)


class ModelDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelDetailSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ModelValidateSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)

#
# class ReviewAPIView(ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
