from django.core.exceptions import ValidationError
from rest_framework import serializers
from form.models import *
from form.api.serializers import *


class ShipmentSerializer(serializers.ModelSerializer):
    base_form = BaseFormSerializer()
    mandatory = MandatorySerializer()
    optional = OptionalSerializer()

    class Meta:
        model = Shipment
        fields = [
            "base_form",
            "mandatory",
            "optional",
            "total_buy",
            "total_sell",
            "profit",
        ]

        extra_kwargs = {
            "base_form": {"allow_null": False, "required": True},
            "mandatory": {"allow_null": False, "required": True},
            "optional": {"allow_null": True, "required": False},
        }

    def create(self, validated_data):
        base_form = validated_data.pop("base_form")
        mandatory = validated_data.pop("mandatory")
        base_form_instance = BaseForm.objects.create(**base_form)
        mandatory_instance = Mandatory.objects.create(**mandatory)
        if base_form_instance.via:
            optional = validated_data.pop("optional")
            optional_instance = Optional.objects.create(**optional)
            shipment = Shipment.objects.create(
                optional=optional_instance,
                base_form=base_form_instance,
                mandatory=mandatory_instance,
                **validated_data
            )
        else:
            try:
                optional = validated_data.pop("optional")
            except KeyError:
                pass
            shipment = Shipment.objects.create(
                optional=None,
                base_form=base_form_instance,
                mandatory=mandatory_instance,
                **validated_data
            )
        return shipment
