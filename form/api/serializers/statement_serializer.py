from rest_framework import serializers
from django.db.models import Max
from form.models import *


class StatemnetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statement
        fields = ["charge", "date", "consignee", "currency"]

    def create(self, validated_data):
        max_order = Statement.objects.aggregate(Max("order"))
        if max_order:
            max_value = max_order["order__max"]
            max_obj = Statement.objects.filter(order=max_value)
            print(max_obj.first())
            
            balance = validated_data["charge"] - (max_obj.first().balance if max_obj.first().balance else 0)
        else:
            max_value = 0
        statement = Statement.objects.create(
            order=max_value,
            charge=validated_data["charge"],
            date=validated_data["date"],
            consignee=validated_data["consignee"],
            currency=validated_data["currency"],
            balance=balance,
        )
        return statement
