from rest_framework import serializers
from accounts.util import random_generator
from accounts.models import *


class ProfileSerializer(serializers.ModelSerializer):
    # readonly is used by default in ModelSerializer
    class Meta:
        model = User
        fields = ['email', 'password', 'nationality', 'first_name', 'last_name', 'phone_number',
                  'company_name', 'validation']
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)

    def validate(self, data):
        data['validation'] = random_generator()
        return data

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            nationality=validated_data['nationality'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            company_name=validated_data['company_name'],
            validation=random_generator()
        )
        # mabey we need it for validation
        user.save()
        user.set_password(validated_data['password'])
        return user
