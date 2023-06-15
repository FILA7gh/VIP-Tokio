from .models import Model, Review
from .serializer import ModelSerializer, ModelValidateSerializer, ReviewSerializer, ReviewValidateSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ModelApiView(ListCreateAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    pagination_class = PageNumberPagination

    def post(self, request, *args, **kwargs):
        serializer = ModelValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        model = Model.objects.create(**serializer.validated_data)
        return Response(data=ModelSerializer(model).data)


class ModelDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    lookup_url_kwarg = 'id_'
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        serializer = ModelValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        model = Model.objects.all()
        model.photo = serializer.validated_data.get('photo')
        model.name = serializer.validated_data.get('name')
        model.age = serializer.validated_data.get('age')
        model.description = serializer.validated_data.get('description')
        model.height = serializer.validated_data.get('height')
        model.weight = serializer.validated_data.get('weight')
        model.is_virgin = serializer.validated_data.get('is_virgin')
        model.price = serializer.validated_data.get('price')
        return Response(data=ModelSerializer(model).data)


class ReviewApiView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination

    def post(self, request, *args, **kwargs):
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review = Review.objects.create(**serializer.validated_data)
        return Response(data=ReviewSerializer(review).data)


class ReviewDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_url_kwarg = 'id_'
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review = Review.objects.all()
        review.stars = serializer.validated_data.get('stars')
        review.text = serializer.validated_data.get('text')
        return Response(data=ReviewSerializer(review).data)
