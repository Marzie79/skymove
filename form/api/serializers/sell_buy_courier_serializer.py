from rest_framework import serializers
from form.models import *


class SellBuyCourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellBuyCourier
        fields = "__all__"
        extra_kwargs = {
            "ups_fee": {"allow_null": True, "required": False},
            "fuel_surcharge_ups": {"allow_null": True, "required": False},
            "fuel_surcharge_ups_percentage": {"allow_null": True, "required": False},
            "eph_ups": {"allow_null": True, "required": False},
            "eph_ups_percentage": {"allow_null": True, "required": False},
            "out_of_area_ups": {"allow_null": True, "required": False},
            "dhl_fee": {"allow_null": True, "required": False},
            "fuel_surcharge_dhl": {"allow_null": True, "required": False},
            "fuel_surcharge_dhl_percentage": {"allow_null": True, "required": False},
            "eph_dhl": {"allow_null": True, "required": False},
            "out_of_area_dhl": {"allow_null": True, "required": False},
            "aramex_fee": {"allow_null": True, "required": False},
            "domestic_transfer_ups": {"allow_null": True, "required": False},
            "eph_domestic": {"allow_null": True, "required": False},
            "tax_for_domestic": {"allow_null": True, "required": False},
        }
