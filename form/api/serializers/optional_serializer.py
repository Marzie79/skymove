from rest_framework import serializers
from form.models import *


class OptionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Optional
        fields = "__all__"
        extra_kwargs = {
            "agency": {"allow_null": True, "required": False},
            "carrier": {"allow_null": True, "required": False},
            "airfreight": {"allow_null": True, "required": False},
            "airway_bill": {"allow_null": True, "required": False},
            "pick_up": {"allow_null": True, "required": False},
            "customs": {"allow_null": True, "required": False},
            "ordino": {"allow_null": True, "required": False},
            "warehouse_fee": {"allow_null": True, "required": False},
            "document_under_our_compnay_name": {"allow_null": True, "required": False},
            "other_charge": {"allow_null": True, "required": False},
        }
