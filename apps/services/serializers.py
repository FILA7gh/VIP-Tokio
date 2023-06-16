from rest_framework import serializers
from .models import *


class BasicServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = BasicService
        fields = '__all__'