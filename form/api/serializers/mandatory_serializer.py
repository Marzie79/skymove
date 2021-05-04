from rest_framework import serializers
from form.models import *


class MandatorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mandatory
        fields = "__all__"
