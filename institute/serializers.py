from rest_framework import serializers
from institute.models import *


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    # date = serializers.DateTimeField(format="%y-%m-%d %H:%M:%S")

    class Meta:
        model = News
        fields = '__all__'
        # read_only_fields = ('date',)
        # fields =  ('id', 'title', 'date' ,'description', 'counter', 'image')


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = ('email', 'phone_number')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class NewsLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetter
        fields = '__all__'
