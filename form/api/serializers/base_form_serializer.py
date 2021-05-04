from rest_framework import serializers
from form.models import *


class BaseFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseForm
        fields = "__all__"
