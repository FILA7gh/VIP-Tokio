from rest_framework import serializers
import re

# from .models import Review
from .models import Model, ModelsGallery
from apps.services.models import BasicService, AdditionalService, Massage, Striptease, SadoMazo, Extreme, PackagePrice
from apps.services.serializers import PackagePriceSerializer, BasicServiceSerializer, AdditionalServiceSerializer, \
    MassageSerializer, StripteaseSerializer, SadoMazoSerializer, ExtremeSerializer


# Gallery
class GallerySerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=True)

    class Meta:
        model = ModelsGallery
        fields = 'model_id photo'.split()


'''Model'''


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['id', 'nickname', 'height', 'weight', 'breast', 'phone_number']


class ModelDetailSerializer(serializers.ModelSerializer):
    gallery = GallerySerializer(many=True)
    package_price = PackagePriceSerializer()
    basic_service = BasicServiceSerializer()
    additional_service = AdditionalServiceSerializer()
    massage = MassageSerializer()
    extreme = ExtremeSerializer()
    sadomazo = SadoMazoSerializer()
    striptease = StripteaseSerializer()

    class Meta:
        model = Model
        fields = ['id', 'gallery', 'nickname', 'phone_number', 'age', 'height', 'weight',
                  'appearance', 'eyes', 'hairs', 'breast', 'description', 'speak_english',
                  'type', 'package_price', 'area', 'schedule', 'basic_service', 'additional_service',
                  'massage', 'striptease', 'sadomazo', 'extreme', 'is_trans', 'in_osh']


class ModelValidateSerializer(serializers.Serializer):
    nickname = serializers.CharField(max_length=100, required=True)
    description = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)
    appearance = serializers.ListField(child=serializers.CharField(required=True))
    height = serializers.IntegerField(required=True)
    weight = serializers.IntegerField(required=True)
    eyes = serializers.ListField(child=serializers.CharField(), required=True)
    hairs = serializers.ListField(child=serializers.CharField(), required=True)
    type = serializers.ListField(child=serializers.CharField(), required=True)
    area = serializers.CharField(max_length=100, required=True)
    breast = serializers.ListField(child=serializers.CharField(), required=True)
    phone_number = serializers.CharField(max_length=16, required=True)
    schedule = serializers.CharField(max_length=19, required=True)
    speak_english = serializers.BooleanField(default=False)
    is_trans = serializers.BooleanField(default=False)
    in_osh = serializers.BooleanField(default=False)

    @staticmethod
    def validate_phone_number(phone_number):
        if not re.match(r'^\+?\d{10,16}$', phone_number):
            raise serializers.ValidationError('Номер телефона не действителен!')
        return phone_number

    @staticmethod
    def validate_age(age):
        if not 17 < age < 45:
            raise serializers.ValidationError('Только девушки или женщины 18-45 лет!')
        return age

    @staticmethod
    def validate_description(description):
        if len(description) < 20:
            raise serializers.ValidationError('Слишком мало информации о себе!, '
                                              'минимум 20 символов!')

        return description

    def create(self, validated_data):
        package_price_data = validated_data.pop('package_price')
        basic_service_data = validated_data.pop('basic_service')
        additional_service_data = validated_data.pop('additional_service')
        massage_data = validated_data.pop('massage')
        sadomazo_data = validated_data.pop('sadomazo')
        striptease_data = validated_data.pop('striptease')
        extreme_data = validated_data.pop('extreme')

        model = Model.objects.create(**validated_data)

        model.package_price = PackagePrice.objects.create(**package_price_data)
        model.basic_service = BasicService.objects.create(**basic_service_data)
        model.additional_service = AdditionalService.objects.create(**additional_service_data)
        model.massage = Massage.objects.create(**massage_data)
        model.sadomazo = SadoMazo.objects.create(**sadomazo_data)
        model.striptease = Striptease.objects.create(**striptease_data)
        model.extreme = Extreme.objects.create(**extreme_data)

        model.save()

        return model

    def update(self, instance, validated_data):
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.description = validated_data.get('description', instance.description)
        instance.age = validated_data.get('age', instance.age)
        instance.appearance = validated_data.get('appearance', instance.appearance)
        instance.height = validated_data.get('height', instance.height)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.eyes = validated_data.get('eyes', instance.eyes)
        instance.hairs = validated_data.get('hairs', instance.hairs)
        instance.type = validated_data.get('type', instance.type)
        instance.area = validated_data.get('area', instance.area)
        instance.breast = validated_data.get('breast', instance.breast)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.schedule = validated_data.get('schedule', instance.schedule)
        instance.speak_english = validated_data.get('speak_english', instance.speak_english)
        instance.is_trans = validated_data.get('is_trans', instance.is_trans)
        instance.in_osh = validated_data.get('in_osh', instance.in_osh)
        instance.package_price = validated_data.get('package_price', instance.package_price)
        instance.basic_service = validated_data.get('basic_service', instance.basic_service)
        instance.additional_service = validated_data.get('additional_service', instance.additional_service)
        instance.massage = validated_data.get('massage', instance.massage)
        instance.extreme = validated_data.get('extreme', instance.extreme)
        instance.sadomazo = validated_data.get('sadomazo', instance.sadomazo)
        instance.save()

        return instance

# class ReviewSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Review
#         fields = ['id', 'username', 'text']
#