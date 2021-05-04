from rest_framework import serializers
from form.models import *


class OptionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Optional
        fields = "__all__"
