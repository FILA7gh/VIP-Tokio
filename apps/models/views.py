from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Model
from .serializers import ModelSerializer, ModelValidateSerializer


class ModelAPIView(ListCreateAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    pagination_class = PageNumberPagination


class ModelDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer



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
