from django.db import models
from django.utils.translation import ugettext_lazy as _

from form.models import BaseForm, Mandatory, Optional


class Shipment(models.Model):
    is_deleted = models.BooleanField(_("Is Deleted"), default=False)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    active = models.BooleanField(_("Active"), default=True)
    base_form = models.ForeignKey(BaseForm, on_delete=models.CASCADE)
    buy_mandatory = models.ForeignKey(
        Mandatory, on_delete=models.CASCADE, related_name="mandatory_buy_form"
    )
    buy_optional = models.ForeignKey(
        Optional,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="optional_buy_form",
    )
    sell_mandatory = models.ForeignKey(
        Mandatory, on_delete=models.CASCADE, related_name="mandatory_sell_form"
    )
    sell_optional = models.ForeignKey(
        Optional,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="optional_sell_form",
    )
    total_buy = models.IntegerField(_("Total Buy"), null=True, blank=True)
    total_sell = models.IntegerField(_("Total Sell"), null=True, blank=True)
    profit = models.IntegerField(_("Profit"), null=True, blank=True)
