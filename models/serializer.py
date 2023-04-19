from rest_framework import serializers
from .models import Model
from rest_framework.exceptions import ValidationError


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = 'photo name age description height weight is_virgin price'.split()


class ModelValidateSerializer(serializers.Serializer):
    photo = serializers.ImageField()
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField(max_value=50)
    description = serializers.CharField()
    height = serializers.FloatField()
    weight = serializers.FloatField()
    is_virgin = serializers.BooleanField()
    price = serializers.FloatField()

    def validate_age(self, age):
        if age < 18:
            raise ValidationError('Только совершеннолетние!!!')
        if age > 49:
            raise ValidationError('Слишком старый!!!')