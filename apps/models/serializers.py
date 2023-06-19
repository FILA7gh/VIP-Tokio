from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Model
from apps.services.models import *


class BasicServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicService
        fields = ['title']


class AdditionalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalService
        fields = ['title']


class MassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Massage
        fields = ['title']


class ExtremeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extreme
        fields = ['title']


class SadoMazoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SadoMazo
        fields = ['title']


class StripteaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Striptease
        fields = ['title']


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = 'photo nickname height weight breast phone_number'.split()


class ModelDetailSerializer(serializers.ModelSerializer):
    # gallery = GallerySerializer(many=True)
    basic_service = BasicServiceSerializer(many=True)
    additional_service = AdditionalServiceSerializer(many=True)
    massage = MassageSerializer(many=True)
    extreme = ExtremeSerializer(many=True)
    sadomazo = SadoMazoSerializer(many=True)
    striptease = StripteaseSerializer(many=True)

    class Meta:
        model = Model
        fields = 'photo nickname phone_number age height weight appearance eyes hairs ' \
                 'breast description speak_english type area schedule basic_service ' \
                 'additional_service massage striptease sadomazo extreme is_trans in_osh'.split()


class ModelValidateSerializer(serializers.Serializer):

    @staticmethod
    def validate_phone_number(phone_number):
        if 10 < len(phone_number) < 16 and not phone_number.isdigit():
            pass

    @staticmethod
    def validate_age(age):
        if 17 < age < 45:
            raise ValidationError('Только девшуки или женщины 18-45 лет!')

    @staticmethod
    def validate_height(height):
        if 150 < height < 190:
            raise ValidationError('Рост строго 150-190!')

    @staticmethod
    def validate_weight(weight):
        if 45 < weight < 70:
            raise ValidationError('Вес строго 45-70')

    @staticmethod
    def validate_description(description):
        if len(description) < 20:
            raise ValidationError('Слишком мало информации о себе!')


# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = 'stars text model_name'.split()
#
#
# class ReviewValidateSerializer(serializers.Serializer):
#     text = serializers.CharField()
