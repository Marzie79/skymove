from rest_framework import serializers
from form.models import *


class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cost
        fields = "__all__"
