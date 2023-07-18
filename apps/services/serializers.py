from rest_framework import serializers
from .models import BasicService, AdditionalService, Massage, Striptease, SadoMazo, Extreme, PackagePrice


class BasicServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicService
        fields = '__all__'


class AdditionalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalService
        fields = '__all__'


class MassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Massage
        fields = '__all__'


class StripteaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Striptease
        fields = '__all__'


class SadoMazoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SadoMazo
        fields = '__all__'


class ExtremeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extreme
        fields = '__all__'


class PackagePriceSerializer(serializers.ModelSerializer):

    apartments_1h = serializers.IntegerField(max_value=1000000, required=False)
    apartments_2h = serializers.IntegerField(max_value=1000000, required=False)
    apartments_night = serializers.IntegerField(max_value=1000000, required=False)
    departure_1h = serializers.IntegerField(max_value=1000000, required=False)
    departure_2h = serializers.IntegerField(max_value=1000000, required=False)
    departure_night = serializers.IntegerField(max_value=1000000, required=False)

    class Meta:
        model = PackagePrice
        fields = '__all__'
