from rest_framework import serializers
from form.models import *


class BaseFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseForm
        fields = "__all__"
        extra_kwargs = {
            "date": {"allow_null": True, "required": False},
            "consignee": {"allow_null": True, "required": False},
            "company_invoice_no": {"allow_null": True, "required": False},
            "consignee_order_no": {"allow_null": True, "required": False},
            "sender": {"allow_null": True, "required": False},
            "reciever": {"allow_null": True, "required": False},
            "currency": {"allow_null": True, "required": False},
            "AWB_no_first": {"allow_null": True, "required": False},
            "AWB_no_second": {"allow_null": True, "required": False},
            "from_in_base": {"allow_null": True, "required": False},
            "to": {"allow_null": True, "required": False},
            "via": {"allow_null": True, "required": False},
            "chargeable_weight": {"allow_null": True, "required": False},
            "gross_weight": {"allow_null": True, "required": False},
        }
