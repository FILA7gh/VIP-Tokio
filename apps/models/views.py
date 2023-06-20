from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Model
from .serializers import ModelSerializer, ModelDetailSerializer, ModelValidateSerializer
from .permissions import *


class ModelAPIView(ListCreateAPIView):
    queryset = Model.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ModelSerializer
        elif self.request.method == 'POST':
            return ModelDetailSerializer

    def post(self, request, *args, **kwargs):
        serializer = ModelValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        model = Model.objects.create(**serializer.validated_data)

        return Response(data=ModelSerializer(model).data)


class ModelDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelDetailSerializer
    permission_classes = [IsAdminOrReadOnly]

    # def get(self, request, *args, **kwargs):
    #     model = self.get_object()
    #     return Response(data=ModelDetailSerializer(model, context={'request': request}).data)

    def put(self, request, *args, **kwargs):
        serializer = ModelValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        model = Model.objects.all()
        serializer.update(model, serializer.validated_data)

        return Response(data=ModelSerializer(model).data)


#
# class ReviewApiView(ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     pagination_class = PageNumberPagination
#
#     def post(self, request, *args, **kwargs):
#         serializer = ReviewValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         review = Review.objects.create(**serializer.validated_data)
#         return Response(data=ReviewSerializer(review).data)
#
#
# class ReviewDetailApiView(RetrieveUpdateDestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     lookup_url_kwarg = 'id_'
#     lookup_field = 'id'
#
#     def put(self, request, *args, **kwargs):
#         serializer = ReviewValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         review = Review.objects.all()
#         review.stars = serializer.validated_data.get('stars')
#         review.text = serializer.validated_data.get('text')
#         return Response(data=ReviewSerializer(review).data)
