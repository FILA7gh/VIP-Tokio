from rest_framework import serializers
import re

# from .models import Review
from .models import Model, ModelsGallery
from apps.services.models import *


# Gallery
class GallerySerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=True)

    class Meta:
        model = ModelsGallery
        fields = 'model_id photo'.split()


'''Services'''


class PackagePriceSerializer(serializers.ModelSerializer):
    apartments_1h = serializers.IntegerField(max_value=1000000)
    apartments_2h = serializers.IntegerField(max_value=1000000)
    apartments_night = serializers.IntegerField(max_value=1000000)
    departure_1h = serializers.IntegerField(max_value=1000000)
    departure_2h = serializers.IntegerField(max_value=1000000)
    departure_night = serializers.IntegerField(max_value=1000000)

    class Meta:
        model = PackagePrice
        fields = '__all__'


class BasicServiceSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)

    class Meta:
        model = BasicService
        fields = ['title']


class AdditionalServiceSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)

    class Meta:
        model = AdditionalService
        fields = ['title']


class MassageSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)

    class Meta:
        model = Massage
        fields = ['title']


class ExtremeSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)

    class Meta:
        model = Extreme
        fields = ['title']


class SadoMazoSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)

    class Meta:
        model = SadoMazo
        fields = ['title']


class StripteaseSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)

    class Meta:
        model = Striptease
        fields = ['title']


'''Model'''


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['id', 'nickname', 'height', 'weight', 'breast', 'phone_number']


class ModelDetailSerializer(serializers.ModelSerializer):
    gallery = GallerySerializer(many=True)
    package_price = PackagePriceSerializer()
    basic_service = BasicServiceSerializer(many=True)
    additional_service = AdditionalServiceSerializer(many=True)
    massage = MassageSerializer(many=True)
    extreme = ExtremeSerializer(many=True)
    sadomazo = SadoMazoSerializer(many=True)
    striptease = StripteaseSerializer(many=True)

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
    package_price = serializers.PrimaryKeyRelatedField(queryset=PackagePrice.objects.all(), required=True)
    basic_service = serializers.PrimaryKeyRelatedField(queryset=BasicService.objects.all(), many=True, required=True)
    additional_service = serializers.PrimaryKeyRelatedField(queryset=AdditionalService.objects.all(),
                                                            many=True, required=False)
    massage = serializers.PrimaryKeyRelatedField(queryset=Massage.objects.all(), many=True, required=False)
    extreme = serializers.PrimaryKeyRelatedField(queryset=Extreme.objects.all(), many=True, required=False)
    sadomazo = serializers.PrimaryKeyRelatedField(queryset=SadoMazo.objects.all(), many=True, required=False)
    striptease = serializers.PrimaryKeyRelatedField(queryset=Striptease.objects.all(), many=True, required=False)

    @staticmethod
    def validate_phone_number(phone_number):
        if not re.match(r'^\+?\d{10,16}$', phone_number):
            raise serializers.ValidationError('Номер телефона действителен')
        return phone_number

    @staticmethod
    def validate_age(age):
        if not 17 < age < 45:
            raise serializers.ValidationError('Только девушки или женщины 18-45 лет!')
        return age

    @staticmethod
    def validate_height(height):
        if not 150 < height < 190:
            raise serializers.ValidationError('Рост строго 150-190!')
        return height

    @staticmethod
    def validate_weight(weight):
        if not 45 < weight < 70:
            raise serializers.ValidationError('Вес строго 45-70')
        return weight

    @staticmethod
    def validate_description(description):
        if len(description) < 20:
            raise serializers.ValidationError('Слишком мало информации о себе!')
        return description

    def create(self, validated_data):
        package_price_data = validated_data.pop('package_price')
        basic_service = validated_data.pop('basic_service', [])
        additional_service = validated_data.pop('additional_service', [])
        massage = validated_data.pop('massage', [])
        extreme = validated_data.pop('extreme', [])
        sadomazo = validated_data.pop('sadomazo', [])
        striptease = validated_data.pop('striptease', [])

        model = Model.objects.create(**validated_data)

        for package_price_item in package_price_data:
            PackagePrice.objects.create(model=model, **package_price_item)

        model.basic_service.set(basic_service)
        model.additional_service.set(additional_service)
        model.massage.set(massage)
        model.extreme.set(extreme)
        model.sadomazo.set(sadomazo)
        model.striptease.set(striptease)

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
        instance.basic_service.set(validated_data.get('basic_service', instance.basic_service.all()))
        instance.additional_service.set(validated_data.get('additional_service', instance.additional_service.all()))
        instance.massage.set(validated_data.get('massage', instance.massage.all()))
        instance.extreme.set(validated_data.get('extreme', instance.extreme.all()))
        instance.sadomazo.set(validated_data.get('sadomazo', instance.sadomazo.all()))
        instance.save()

        return instance

# class ReviewSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Review
#         fields = ['id', 'username', 'text']
