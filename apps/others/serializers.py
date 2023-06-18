from rest_framework import serializers
from .models import *


class SupportSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20)
    mail = serializers.EmailField(max_length=50)
    subject = serializers.CharField(max_length=20)

    class Meta:
        model = Support
        fields = '__all__'


class MiniBlogSerializer(serializers.ModelSerializer):
    title = models.CharField(max_length=30)
    image = models.ImageField()
    description = models.TextField()

    class Meta:
        model = MiniBlog
        fields = '__all__'


class MiniBlogDetailSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MiniBlog
        fields = ['id', 'title', 'image', 'description', 'user']


class AboutUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MiniBlog
        fields = '__all__'


class AboutUsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = MiniBlog
        fields = '__all__'
