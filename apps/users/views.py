from .serializers import UserCreateValidateSerializer, UserLoginSerializer, \
    UserConfirmSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.views import APIView
from random import randint
from .models import ConfirmationCode


class RegistrationApiView(APIView):
    def post(self, request):
        serializer = UserCreateValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        code = ''
        for i in range(6):
            code += str(randint(0, 9))

        user = User.objects.create_user(**serializer.validated_data)
        code = ConfirmationCode.objects.create(user_id=user.id, code=code)
        return Response(data={'user_id': user.id, 'code': code.code})


class ConfirmApiView(APIView):
    def post(self, request):
        serializer = UserConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if ConfirmationCode.objects.filter(user_id=request.data['user_id'], code=request.data['code']):
            return Response(data={'confirm': 'success'})

        return Response(data={'error': 'wrong id or code!'})


class AuthorizationApiView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})

        return Response(data={'error': 'wrong Username or Password!'})
    