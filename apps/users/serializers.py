from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
import re
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class YourTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # Дополнительная логика, если необходимо
        token = super().get_token(user)
        # Дополнительная логика, если необходимо
        return token


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    username = serializers.CharField(min_length=4)
    password = serializers.CharField()
    password2 = serializers.CharField()
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    email2 = serializers.EmailField()

    @staticmethod
    def validate_username(username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        return ValidationError('user already exist!')

    @staticmethod
    def validate_password(password):
        if re.match("^(?=.*?[a-z])(?=.*?[0-9]).{8,}$", password):
            return password
        raise ValidationError('The password must consist of at least letters and numbers!')

    def create(self, validated_data):
        validated_data['is_active'] = False
        first_name = validated_data.get('first_name')
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        user = User.objects.create_user(first_name=first_name, username=username,
                                        password=password, email=email)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=4)
    password = serializers.CharField()


class ResetSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetConfirmPasswordSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField()


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    password_2 = serializers.CharField()

    @staticmethod
    def validate_password(password):
        if re.match("^(?=.*?[a-z])(?=.*?[0-9]).{8,}$", password):
            return password
        raise ValidationError('The password must consist of at least letters and numbers!')
