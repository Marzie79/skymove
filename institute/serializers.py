from rest_framework import serializers
from institute.models import *


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ('name', 'phone_number', 'email', 'message',)


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ABoutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ABoutUs
        fields = '__all__'
