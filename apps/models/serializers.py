from rest_framework import serializers
from .models import Model
from rest_framework.exceptions import ValidationError


class ModelSerializer(serializers.ModelSerializer):
    # gallery = GallerySerializer(many=True)
    # appearance = serializers.ChoiceField(choices=Model.CHOICE_APPEARANCE)

    class Meta:
        model = Model
        fields = 'photo description nickname age appearance height weight eyes hairs ' \
                 'type area breast phone_number schedule speak_english is_trans in_osh'.split()


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


# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = 'stars text model_name'.split()
#
#
# class ReviewValidateSerializer(serializers.Serializer):
#     text = serializers.CharField()
