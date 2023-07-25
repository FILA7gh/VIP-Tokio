from rest_framework import serializers
import re
from drf_writable_nested.serializers import WritableNestedModelSerializer

from .models import Model, Review
from apps.services.models import BasicService, AdditionalService, Massage, Striptease, SadoMazo, Extreme, PackagePrice
from apps.services.serializers import PackagePriceSerializer, BasicServiceSerializer, AdditionalServiceSerializer, \
    MassageSerializer, StripteaseSerializer, SadoMazoSerializer, ExtremeSerializer


'''Model'''


class ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Model
        fields = ['id', 'photo_1', 'nickname', 'height', 'weight', 'breast', 'phone_number']


class ModelDetailSerializer(serializers.ModelSerializer):
    package_price = PackagePriceSerializer(required=False)
    basic_service = BasicServiceSerializer(many=True, required=False)
    additional_service = AdditionalServiceSerializer(many=True, required=False)
    massage = MassageSerializer(many=True, required=False)
    extreme = ExtremeSerializer(many=True, required=False)
    sadomazo = SadoMazoSerializer(many=True, required=False)
    striptease = StripteaseSerializer(many=True, required=False)

    class Meta:
        model = Model
        fields = ['id', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6', 'photo_7',
                  'nickname', 'phone_number', 'age', 'height', 'weight',
                  'appearance', 'eyes', 'hairs', 'breast', 'description', 'speak_english',
                  'type', 'package_price', 'area', 'schedule', 'basic_service', 'additional_service',
                  'massage', 'striptease', 'sadomazo', 'extreme', 'is_trans', 'country']



class ModelValidateSerializer(WritableNestedModelSerializer):
    nickname = serializers.CharField(max_length=100, required=True)
    description = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)
    appearance = serializers.CharField(max_length=20, required=True)
    height = serializers.IntegerField(required=True)
    weight = serializers.IntegerField(required=True)
    eyes = serializers.CharField(max_length=20, required=True)
    hairs = serializers.CharField(max_length=20, required=True)
    type = serializers.CharField(max_length=20, required=True)
    area = serializers.CharField(max_length=100, required=True)
    breast = serializers.CharField(max_length=20, required=True)
    phone_number = serializers.CharField(max_length=16, required=True)
    schedule = serializers.CharField(max_length=19, required=True)
    speak_english = serializers.BooleanField(default=False)
    is_trans = serializers.BooleanField(default=False)
    country = serializers.CharField(max_length=100, default='Бишкек')
    photo_1 = serializers.ImageField(required=True)
    photo_2 = serializers.ImageField(required=False)
    photo_3 = serializers.ImageField(required=False)
    photo_4 = serializers.ImageField(required=False)
    photo_5 = serializers.ImageField(required=False)
    photo_6 = serializers.ImageField(required=False)
    photo_7 = serializers.ImageField(required=False)

    package_price = PackagePriceSerializer(required=False)

    basic_service = serializers.PrimaryKeyRelatedField(queryset=BasicService.objects.all(), many=True, required=True)
    additional_service = serializers.PrimaryKeyRelatedField(queryset=AdditionalService.objects.all(),
                                                            many=True, required=False)
    massage = serializers.PrimaryKeyRelatedField(queryset=Massage.objects.all(), many=True, required=False)
    extreme = serializers.PrimaryKeyRelatedField(queryset=Extreme.objects.all(), many=True, required=False)
    sadomazo = serializers.PrimaryKeyRelatedField(queryset=SadoMazo.objects.all(), many=True, required=False)
    striptease = serializers.PrimaryKeyRelatedField(queryset=Striptease.objects.all(), many=True, required=False)

    class Meta:
        model = Model
        fields = '__all__'

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
            package_price = validated_data.pop('package_price')
            basic_services = validated_data.pop('basic_service')
            additional_services = validated_data.pop('additional_service')
            massages = validated_data.pop('massage')
            extremes = validated_data.pop('extreme')
            sado_mazos = validated_data.pop('sado_mazo')
            stripteazes = validated_data.pop('stripteaze')

            model = Model.objects.create(package_price=package_price, **validated_data)

            for basic_service in basic_services:
                BasicService.objects.add(model=model, **basic_service)
            for additional_service in additional_services:
                AdditionalService.objects.add(model=model, **additional_service)
            for massage in massages:
                Massage.objects.add(model=model, **massage)
            for extreme in extremes:
                Extreme.objects.add(model=model, **extreme)
            for sado_mazo in sado_mazos:
                SadoMazo.objects.add(model=model, **sado_mazo)
            for stripteaze in stripteazes:
                Striptease.objects.add(model=model, **stripteaze)

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
            instance.country = validated_data.get('country', instance.country)
            instance.photo_1 = validated_data.get('photo_1', instance.photo_1)
            instance.photo_2 = validated_data.get('photo_2', instance.photo_2)
            instance.photo_3 = validated_data.get('photo_3', instance.photo_3)
            instance.photo_4 = validated_data.get('photo_4', instance.photo_4)
            instance.photo_5 = validated_data.get('photo_5', instance.photo_5)
            instance.photo_6 = validated_data.get('photo_6', instance.photo_6)
            instance.photo_7 = validated_data.get('photo_7', instance.photo_7)

            package_price = validated_data.pop('package_price')
            basic_services = validated_data.pop('basic_service')
            additional_services = validated_data.pop('additional_service')
            massages = validated_data.pop('massage')
            extremes = validated_data.pop('extreme')
            sado_mazos = validated_data.pop('sado_mazo')
            stripteazes = validated_data.pop('stripteaze')

            instance.package_price.set(package_price)
            instance.basic_service.set(basic_services)
            instance.additional_service.set(additional_services)
            instance.massage.set(massages)
            instance.extreme.set(extremes)
            instance.sado_mazo.set(sado_mazos)
            instance.stripteaze.set(stripteazes)

            instance.save()
            return instance


class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, max_length=50)
    text = serializers.CharField(required=True)

    class Meta:
        model = Review
        fields = ['id', 'username', 'text']
