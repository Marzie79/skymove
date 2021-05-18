from django.core.exceptions import ValidationError
from rest_framework import serializers
from form.models import *
from form.api.serializers import *


class CourierSerializer(serializers.ModelSerializer):
    base_form_courier = BaseFormCourierSerializer()
    sell = SellBuyCourierSerializer()
    buy = SellBuyCourierSerializer()

    class Meta:
        model = Courier
        fields = [
            "base_form_courier",
            "sell",
            "buy",
            "total_buy",
            "total_sell",
            "custom_clearnace_buy",
            "custom_clearnace_sell",
            "profit_sell",
            "profit_sell_percentage",
            "profit",
        ]
        read_only_fields = ("total_buy", "total_sell", "profit")
        extra_kwargs = {
            "base_form_courier": {"allow_null": False, "required": True},
            "sell": {"allow_null": False, "required": True},
            "buy": {"allow_null": False, "required": True},
            "custom_clearnace_buy": {"allow_null": False, "required": True},
            "custom_clearnace_sell": {"allow_null": False, "required": True},
            "profit_sell": {"allow_null": False, "required": True},
            "profit_sell_percentage": {"allow_null": True, "required": False},
        }

    def create(self, validated_data):
        base_form_courier = validated_data.pop("base_form_courier")
        base_form_courier_instance = BaseFormCourier.objects.create(**base_form_courier)
        sell = validated_data.pop("sell")
        sell_instance = SellBuyCourier.objects.create(**sell)
        buy = validated_data.pop("buy")
        buy_instance = SellBuyCourier.objects.create(**buy)

        if (
            not base_form_courier_instance.pk
            or not sell_instance.pk
            or not buy_instance.pk
        ):
            raise ValidationError("data is not correct")
        total_buy = (
            buy_instance.ups_fee
            + buy_instance.fuel_surcharge_ups
            + buy_instance.eph_ups
            + buy_instance.out_of_area_ups
            + buy_instance.dhl_fee
            + buy_instance.fuel_surcharge_dhl
            + buy_instance.eph_dhl
            + buy_instance.out_of_area_dhl
            + buy_instance.aramex_fee
            + buy_instance.domestic_transfer_ups
            + buy_instance.eph_domestic
            + buy_instance.tax_for_domestic
            + validated_data["custom_clearnace_buy"]
        )
        total_sell = (
            sell_instance.ups_fee
            + sell_instance.fuel_surcharge_ups
            + sell_instance.eph_ups
            + sell_instance.out_of_area_ups
            + sell_instance.dhl_fee
            + sell_instance.fuel_surcharge_dhl
            + sell_instance.eph_dhl
            + sell_instance.out_of_area_dhl
            + sell_instance.aramex_fee
            + sell_instance.domestic_transfer_ups
            + sell_instance.eph_domestic
            + sell_instance.tax_for_domestic
            + validated_data["custom_clearnace_sell"]
            + validated_data["profit_sell"]
        )
        courier = Courier.objects.create(
            sell=sell_instance,
            buy=buy_instance,
            base_form_courier=base_form_courier_instance,
            total_buy=total_buy,
            total_sell=total_sell,
            profit=total_sell - total_buy,
            **validated_data
        )
        return courier
