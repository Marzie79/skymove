from rest_framework import serializers
from form.models import *


class MandatorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mandatory
        fields = "__all__"
        extra_kwargs = {
            "agency": {"allow_null": True, "required": False},
            "carrier": {"allow_null": True, "required": False},
            "airfreight": {"allow_null": True, "required": False},
            "airway_bill": {"allow_null": True, "required": False},
            "pick_up": {"allow_null": True, "required": False},
            "customs": {"allow_null": True, "required": False},
            "sbl": {"allow_null": True, "required": False},
            "other_charge": {"allow_null": True, "required": False},
        }
