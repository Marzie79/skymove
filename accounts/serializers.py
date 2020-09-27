from django.utils.encoding import force_text
from rest_framework import serializers, status
from rest_framework.exceptions import APIException
from rest_framework.serializers import raise_errors_on_nested_writes
from validate_email import validate_email

from accounts.models import *


class LogInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)


class ValidationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(allow_blank=True, allow_null=True)
    validation = serializers.CharField(max_length=6)


class EmailAddressSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ProfileSerializer(serializers.ModelSerializer):
    # readonly is used by default in ModelSerializer
    class Meta:
        model = User
        fields = ['email', 'password', 'nationality', 'first_name', 'last_name', 'phone_number',
                  'company_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # check that email is valid in internet
        # is_valid = validate_email(validated_data['email'])
        # if not is_valid:
        #     # if email is not valid in internet return 406 status code
        #     raise CustomValidation('email is not exist', 'email', status_code=status.HTTP_406_NOT_ACCEPTABLE)
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        if 'email' in validated_data:
            raise CustomValidation('email is not exist', 'email', status_code=status.HTTP_406_NOT_ACCEPTABLE)
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.attr = instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class CustomValidation(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'A server error occurred.'

    def __init__(self, detail, field, status_code):
        if status_code is not None: self.status_code = status_code
        if detail is not None:
            self.detail = {field: force_text(detail)}
        else:
            self.detail = {'detail': force_text(self.default_detail)}
