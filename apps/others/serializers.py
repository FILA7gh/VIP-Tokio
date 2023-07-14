from rest_framework import serializers
from .models import Support, MiniBlog, AboutUs, DidYouKnow, Help, MiniBlogGallery, Rules, Contact


class SupportSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, required=True)
    mail = serializers.EmailField(max_length=100, required=True)
    subject = serializers.CharField(max_length=100, required=True)
    message = serializers.CharField()

    class Meta:
        model = Support
        fields = '__all__'


class MiniBlogGallerySerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)

    class Meta:
        model = MiniBlogGallery
        fields = ['mini_blog_id', 'photo']


class MiniBlogSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=30, required=True)
    text = serializers.CharField(required=True)
    gallery = MiniBlogGallerySerializer(many=True, required=False)

    class Meta:
        model = MiniBlog
        fields = ['id', 'title', 'text', 'gallery']


class AboutUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutUs
        fields = '__all__'


class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = '__all__'


class DidYouKnowSerializer(serializers.ModelSerializer):
    class Meta:
        model = DidYouKnow
        fields = '__all__'


class RulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rules
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
