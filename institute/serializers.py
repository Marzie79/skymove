from rest_framework import serializers
from institute.models import *


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = ('email', 'phone_number')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
