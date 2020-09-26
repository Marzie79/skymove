from rest_framework import serializers
from home.models import *


class NewsLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetter
        fields = '__all__'


class HomeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeVideo
        fields = '__all__'


class ABoutUsPicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ABoutUsHomeSlideShow
        fields = ('image',)


class ABoutUsHomeSerializer(serializers.ModelSerializer):
    pictures = ABoutUsPicturesSerializer(many=True, read_only=True)

    class Meta:
        model = ABoutUsHome
        fields = ('description', 'title', 'pictures')
