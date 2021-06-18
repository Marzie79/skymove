from django.db import models
from django.utils.translation import ugettext_lazy as _


class Statement(models.Model):
    USD = "usd"
    EUR = "eur"
    TRY = "try"
    CURRENCY_STATUS = ((USD, "usd"), (EUR, "eur"), (TRY, "try"))

    shipment = models.ForeignKey(
        "form.Shipment", blank=True, null=True, on_delete=models.SET_NULL
    )
    courier = models.ForeignKey(
        "form.Courier", blank=True, null=True, on_delete=models.SET_NULL
    )
    consignee = models.ForeignKey(
        "form.Consignee", null=True, blank=True, on_delete=models.SET_NULL
    )
    charge = models.FloatField(null=True, blank=True, max_length=255)
    balance = models.FloatField(null=True, blank=True, max_length=255)
    currency = models.CharField(
        null=True, blank=True, max_length=255, choices=CURRENCY_STATUS
    )
    order = models.IntegerField(null=True, blank=True, default=0)
    date = models.DateField(_("Date"), blank=True, null=True)
