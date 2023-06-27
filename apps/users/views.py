from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from django.core.mail import EmailMessage
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from random import randint
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from .serializers import RegisterSerializer, LoginSerializer, ResetSerializer, \
    ResetConfirmPasswordSerializer, ChangePasswordSerializer, YourTokenObtainPairSerializer
from .models import ResetPasswordConfirm

from rest_framework_simplejwt.views import TokenObtainPairView


class ObtainTokenPairView(TokenObtainPairView):
    serializer_class = YourTokenObtainPairSerializer


class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    host_user = 'settings.base.EMAIL_HOST_USER'

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.is_staff = False
        user.save()
        password = serializer.validated_data.get('password')
        password2 = serializer.validated_data.get('password2')

        if password != password2:
            raise ValidationError('Пароли не совпадают!')

        email = serializer.validated_data.get('email')
        email2 = serializer.validated_data.get('email2')

        if email != email2:
            raise ValidationError('Почты не совпадают!')

        send_email = EmailMessage(f'Параметры учётной записи для {user.first_name} '
                                  f'на сайте VIP Tokio проститутки Токтогула',
                                  f'Здравствуйте {user.first_name}\n'
                                  f'Спасибо за регистрацию на VIP Tokio проститутки Токтогула.\n'
                                  f'Теперь вы можете войти на https://vip-tokio.com/ используя следующие данные:\n'
                                  f'Логин: {user.username}\nПароль: {user.password}',
                                  from_email=self.host_user, to=[email])
        if send_email.send():
            return Response(data='Сообщение\n'
                                 'Спасибо за регистрацию. Теперь вы можете войти на сайт, '
                                 'используя логин и пароль, указанные при регистрации.',
                            status=status.HTTP_201_CREATED)
        user.delete()
        return Response(data=f'Problem sending email to {email}, check if you typed it correctly',
                        status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            refresh = RefreshToken.for_user(user)
            access = AccessToken.for_user(user)
            return Response({
                'user': user.username,
                'token': str(refresh),
                'access_token': str(access)
            })

        return Response(data='Неправильный логин или пароль!', status=status.HTTP_401_UNAUTHORIZED)


class ResetAPIVIew(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ResetSerializer
    permission_classes = [AllowAny]
    host_user = 'settings.base.EMAIL_HOST_USER'


class ResetLoginAPIView(ResetAPIVIew):
    def post(self, request, *args, **kwargs):

        user_id = self.kwargs['pk']
        get_object_or_404(User, id=user_id)
        # Если пользователь с указанным идентификатором не найден,
        # будет сгенерировано исключение Http404

        email = request.data.get('email')
        user = get_object_or_404(User, email=email)

        send_email = EmailMessage('Восстановление логина на сайте VIP Tokio проститутки Токтогула',
                                  f'Здравствуйте, На сайте VIP Bishkek проститутки Бишкека была сделана '
                                  f'заявка на восстановление логина вашей учётной записи.\n'
                                  f'Ваш логин: {user.username}.\n'
                                  f'Для входа на сайт под вашими учётными данными перейдите по ссылке ниже.\n'
                                  f'https://vip-tokio.com/register?view=login\nСпасибо.',
                                  from_email=self.host_user, to=[email])

        if send_email.send():
            return Response(data={'message': 'Сообщение с информацией отправлено на указанный адрес. '
                                             'Пожалуйста, проверьте почту.'},
                            status=status.HTTP_200_OK)

        return Response(data='Не удалось отправить письмо для восстановления логина.',
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ResetPasswordAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ResetSerializer
    permission_classes = [AllowAny]
    host_user = 'settings.base.EMAIL_HOST_USER'

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(data={'detail': 'Почта не найдена!'})

        code = ResetPasswordConfirm.objects.create(username=user.username, code=str(randint(100000, 1000000)))
        print(code.username, code.code)
        send_email = EmailMessage('Запрос сброса пароля на сайте VIP Tokio проститутки Токтогула',
                                  f'Здравствуйте,\n На сайте VIP Tokio проститутки был сделан запрос на '
                                  f'восстановление пароля к вашей учётной записи. Чтобы восстановить пароль'
                                  f' вам потребуется ввести указанный ниже код подтверждения.\n'
                                  f'Код подтверждения: {code.code}.\n'
                                  f'Для ввода кода подтверждения перейдите на страницу по ссылке ниже.\n'
                                  f'https://vibish.com/reset?layout=confirm&token\nСпасибо.',
                                  from_email=self.host_user, to=[email])

        if send_email.send():
            return Response(data='На ваш адрес электронной почты было отправлено письмо, содержащее проверочный код.'
                                 ' Введите его, пожалуйста, в поле ниже. '
                                 'Это подтвердит, что именно вы являетесь владельцем данной учётной записи.',
                            status=status.HTTP_200_OK)

        return Response(data='Не удалось отправить письмо для восстановления пароля.',
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ResetConfirmPasswordAPIView(CreateAPIView):
    queryset = ResetPasswordConfirm.objects.all()
    serializer_class = ResetConfirmPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data.get('username')
        code = request.data.get('code')

        try:
            ResetPasswordConfirm.objects.get(username=username, code=code)
        except ResetPasswordConfirm.DoesNotExist:
            return Response(data={'detail': 'Не удалось восстановить пароль, поскольку проверочный код'
                                            ' был указан неверно. Пользователь не найден!'},
                            status=status.HTTP_404_NOT_FOUND)

        return Response(data={'detail': 'success'}, status=status.HTTP_200_OK)


class ChangePasswordAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = self.kwargs['pk']

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(data={'detail': 'ID пользователя не найден!'})

        password = request.data.get('password')
        password_2 = request.data.get('password_2')

        if password != password_2:
            raise ValidationError('Пароли не совпадают!')

        user.set_password(password)  # Используем set_password() для изменения пароля
        user.save()

        return Response(data={'detail': 'Пароль успешно изменен'})
