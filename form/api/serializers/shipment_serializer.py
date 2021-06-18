from django.core.exceptions import ValidationError
from rest_framework import serializers
from form.models import *
from form.api.serializers import *


class ShipmentSerializer(serializers.ModelSerializer):
    base_form = BaseFormSerializer()
    sell_mandatory = MandatorySerializer()
    sell_optional = OptionalSerializer()
    buy_mandatory = MandatorySerializer()
    buy_optional = OptionalSerializer()

    class Meta:
        model = Shipment
        fields = [
            "base_form",
            "sell_mandatory",
            "sell_optional",
            "buy_mandatory",
            "buy_optional",
            "total_buy",
            "total_sell",
            "profit",
        ]
        read_only_fields = ("total_buy", "total_sell", "profit")
        extra_kwargs = {
            "base_form": {"allow_null": False, "required": True},
            "sell_mandatory": {"allow_null": False, "required": True},
            "sell_optional": {"allow_null": True, "required": False},
            "buy_mandatory": {"allow_null": False, "required": True},
            "buy_optional": {"allow_null": True, "required": False},
        }

    def create(self, validated_data):
        base_form = validated_data.pop("base_form")
        sell_mandatory = validated_data.pop("sell_mandatory")
        buy_mandatory = validated_data.pop("buy_mandatory")
        sell_mandatory_instance = Mandatory.objects.create(**sell_mandatory)
        buy_mandatory_instance = Mandatory.objects.create(**buy_mandatory)
        if not sell_mandatory_instance.pk and not buy_mandatory_instance.pk:
            raise ValidationError("data is not correct")

        total_buy = (
            buy_mandatory_instance.airfreight
            + buy_mandatory_instance.airway_bill
            + buy_mandatory_instance.pick_up
            + buy_mandatory_instance.customs
            + buy_mandatory_instance.sbl
            + buy_mandatory_instance.customs
        )
        total_sell = (
            sell_mandatory_instance.airfreight
            + sell_mandatory_instance.airway_bill
            + sell_mandatory_instance.pick_up
            + sell_mandatory_instance.customs
            + sell_mandatory_instance.sbl
            + sell_mandatory_instance.customs
        )

        base_form_instance = BaseForm.objects.create(**base_form)
        if base_form_instance.via:
            sell_optional = validated_data.pop("sell_optional")
            sell_optional_instance = Optional.objects.create(**sell_optional)
            buy_optional = validated_data.pop("buy_optional")
            buy_optional_instance = Optional.objects.create(**buy_optional)
            if not buy_optional_instance.pk and not sell_optional_instance.pk:
                raise ValidationError("data is not correct")
            total_buy = (
                total_buy
                + buy_optional_instance.airfreight
                + buy_optional_instance.airway_bill
                + buy_optional_instance.pick_up
                + buy_optional_instance.customs
                + buy_optional_instance.ordino
                + buy_optional_instance.warehouse_fee
                + buy_optional_instance.document_under_our_compnay_name
                + buy_optional_instance.other_charge
                + buy_optional_instance.other_charge_second
            )
            total_sell = (
                total_sell
                + sell_optional_instance.airfreight
                + sell_optional_instance.airway_bill
                + sell_optional_instance.pick_up
                + sell_optional_instance.customs
                + sell_optional_instance.ordino
                + sell_optional_instance.warehouse_fee
                + sell_optional_instance.document_under_our_compnay_name
                + sell_optional_instance.other_charge
                + sell_optional_instance.other_charge_second
            )
            shipment = Shipment.objects.create(
                sell_optional=sell_optional_instance,
                buy_optional=buy_optional_instance,
                base_form=base_form_instance,
                sell_mandatory=sell_mandatory_instance,
                buy_mandatory=buy_mandatory_instance,
                total_buy=total_buy,
                total_sell=total_sell,
                profit=total_sell - total_buy,
            )
        else:
            try:
                sell_optional = validated_data.pop("sell_optional")
                buy_optional = validated_data.pop("buy_optional")
            except KeyError:
                pass
            shipment = Shipment.objects.create(
                sell_optional=None,
                buy_optional=None,
                base_form=base_form_instance,
                sell_mandatory=sell_mandatory_instance,
                buy_mandatory=buy_mandatory_instance,
                total_buy=total_buy,
                total_sell=total_sell,
                profit=total_sell - total_buy,
            )
        return shipment


    def update(self, instance, validated_data):
        base_form = validated_data.pop("base_form")
        sell_mandatory = validated_data.pop("sell_mandatory")
        buy_mandatory = validated_data.pop("buy_mandatory")
        for key, value in sell_mandatory.items():
            setattr(instance.sell_mandatory, key, value)
        instance.sell_mandatory.save()
        for key, value in buy_mandatory.items():
            setattr(instance.buy_mandatory, key, value)
        instance.buy_mandatory.save()
        
        total_buy = (
            instance.buy_mandatory.airfreight
            + instance.buy_mandatory.airway_bill
            + instance.buy_mandatory.pick_up
            + instance.buy_mandatory.customs
            + instance.buy_mandatory.sbl
            + instance.buy_mandatory.customs
        )
        total_sell = (
            instance.sell_mandatory.airfreight
            + instance.sell_mandatory.airway_bill
            + instance.sell_mandatory.pick_up
            + instance.sell_mandatory.customs
            + instance.sell_mandatory.sbl
            + instance.sell_mandatory.customs
        )
        for key, value in base_form.items():
            setattr(instance.base_form, key, value)
        instance.base_form.save()

        if instance.base_form.via:
            if not instance.sell_optional:
                sell_optional = validated_data.pop("sell_optional")
                sell_optional_instance = Optional.objects.create(**sell_optional)
                buy_optional = validated_data.pop("buy_optional")
                buy_optional_instance = Optional.objects.create(**buy_optional)
                if not buy_optional_instance.pk and not sell_optional_instance.pk:
                    raise ValidationError("data is not correct")
                total_buy = (
                    total_buy
                    + buy_optional_instance.airfreight
                    + buy_optional_instance.airway_bill
                    + buy_optional_instance.pick_up
                    + buy_optional_instance.customs
                    + buy_optional_instance.ordino
                    + buy_optional_instance.warehouse_fee
                    + buy_optional_instance.document_under_our_compnay_name
                    + buy_optional_instance.other_charge
                    + buy_optional_instance.other_charge_second
                )
                total_sell = (
                    total_sell
                    + sell_optional_instance.airfreight
                    + sell_optional_instance.airway_bill
                    + sell_optional_instance.pick_up
                    + sell_optional_instance.customs
                    + sell_optional_instance.ordino
                    + sell_optional_instance.warehouse_fee
                    + sell_optional_instance.document_under_our_compnay_name
                    + sell_optional_instance.other_charge
                    + sell_optional_instance.other_charge_second
                )
            else:
                sell_optional = validated_data.pop("sell_optional")
                for key, value in sell_optional.items():
                    setattr(instance.sell_optional, key, value)
                instance.sell_optional.save()        
                buy_optional = validated_data.pop("buy_optional")
                for key, value in buy_optional.items():
                    setattr(instance.buy_optional, key, value)
                instance.buy_optional.save()   
                total_buy = (
                    total_buy
                    + instance.buy_optional.airfreight
                    + instance.buy_optional.airway_bill
                    + instance.buy_optional.pick_up
                    + instance.buy_optional.customs
                    + instance.buy_optional.ordino
                    + instance.buy_optional.warehouse_fee
                    + instance.buy_optional.document_under_our_compnay_name
                    + instance.buy_optional.other_charge
                    + instance.buy_optional.other_charge_second
                )
                total_sell = (
                    total_sell
                    + instance.sell_optional.airfreight
                    + instance.sell_optional.airway_bill
                    + instance.sell_optional.pick_up
                    + instance.sell_optional.customs
                    + instance.sell_optional.ordino
                    + instance.sell_optional.warehouse_fee
                    + instance.sell_optional.document_under_our_compnay_name
                    + instance.sell_optional.other_charge
                    + instance.sell_optional.other_charge_second
                )
        else:
            try:
                sell_optional = validated_data.pop("sell_optional")
                buy_optional = validated_data.pop("buy_optional")
            except KeyError:
                pass
        instance.save()
        return instance