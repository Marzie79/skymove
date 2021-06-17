from rest_framework import serializers
from form.models import *


class ConsigneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consignee
        fields = "__all__"
