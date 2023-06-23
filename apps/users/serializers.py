from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserValidateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField()


class UserCreateValidateSerializer(UserValidateSerializer):

    def validate_name(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('user already exists!')

    def validate_password(self, password):
        if len(password) < 8 or password.isdigit() or password.isalpha():
            raise ValidationError('bad password!')
        else:
            return password


class UserLoginSerializer(UserValidateSerializer):
    pass


class UserConfirmSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = 'user_id code'.split()



