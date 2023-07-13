from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Model
from .serializers import ModelSerializer, ModelDetailSerializer, ModelValidateSerializer
from .permissions import *


class ModelAPIView(ListCreateAPIView):
    queryset = Model.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ModelSerializer
        elif self.request.method == 'POST':
            return ModelDetailSerializer

    def post(self, request, *args, **kwargs):
        serializer = ModelValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        model = Model.objects.create(**serializer.validated_data)

        model.package_price = serializer.validated_data['package_price']
        model.basic_service.set(serializer.validated_data['basic_services'])
        model.additional_service.set(serializer.validated_data['additional_service'])
        model.massage.set(serializer.validated_data['massage'])
        model.extreme.set(serializer.validated_data['extreme'])
        model.sadomazo.set(serializer.validated_data['sadomazo'])
        model.striptease.set(serializer.validated_data['striptease'])
        model.save()

        return Response(data=ModelSerializer(model, context={'request': request}).data)


class ModelDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def put(self, request, *args, **kwargs):
        serializer = ModelValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        model = self.get_object()

        package_price = serializer.validated_data.get('package_price')
        basic_service = serializer.validated_data.pop('basic_service', [])
        additional_service = serializer.validated_data.pop('additional_service', [])
        massage = serializer.validated_data.pop('massage', [])
        extreme = serializer.validated_data.pop('extreme', [])
        sadomazo = serializer.validated_data.pop('sadomazo', [])
        striptease = serializer.validated_data.pop('striptease', [])

        serializer.save(package_price=package_price, basic_service=basic_service,
                        additional_service=additional_service, massage=massage,
                        extreme=extreme, sadomazo=sadomazo, striptease=striptease)

        return Response(data=ModelSerializer(model).data)

#
# class ReviewAPIView(ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
