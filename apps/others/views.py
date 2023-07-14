from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from apps.models.permissions import IsAdminOrReadOnly
from .models import AboutUs
from apps.users.utils import send_email


class SupportAPIView(CreateAPIView):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        send_email(subject='Поддержка',
                   body=f"Имя: {serializer.validated_data['name']} \n"
                        f"Почта: {serializer.validated_data['mail']} \n"
                        f"Тема: {serializer.validated_data['subject']} \n\n"
                        f"{serializer.validated_data['message']}",
                   to_email=('akmatbekovvv@gmail.com',))

        return Response(data={'detail': 'Ваше сообщение отправлено, в скором времени мы вам ответим.'},
                        status=status.HTTP_201_CREATED)


class MiniBlogViewSet(ModelViewSet):
    queryset = MiniBlog.objects.all()
    serializer_class = MiniBlogSerializer
    permission_classes = [IsAdminOrReadOnly]


class AboutUsAPIView(ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAdminOrReadOnly]


class HelpAPIView(ListCreateAPIView):
    queryset = Help.objects.all()
    serializer_class = HelpSerializer
    permission_classes = [IsAdminOrReadOnly]


class DidYouKnowAPIView(ListCreateAPIView):
    queryset = Help.objects.all()
    serializer_class = DidYouKnowSerializer
    permission_classes = [IsAdminOrReadOnly]


class RulesAPIView(ListCreateAPIView):
    queryset = Rules.objects.all()
    serializer_class = RulesSerializer
    permission_classes = [IsAdminOrReadOnly]


class ContactAPIView(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAdminOrReadOnly]
