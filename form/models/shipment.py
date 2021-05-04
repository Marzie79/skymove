from django.db import models
from django.utils.translation import ugettext_lazy as _

from form.models import BaseForm, Mandatory, Optional


class Shipment(models.Model):
    is_deleted = models.BooleanField(_("Is Deleted"), default=False)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    active = models.BooleanField(_("Active"), default=True)
    base_form = models.ForeignKey(BaseForm, on_delete=models.CASCADE)
    mandatory = models.ForeignKey(Mandatory, on_delete=models.CASCADE)
    optional = models.ForeignKey(
        Optional, on_delete=models.SET_NULL, null=True, blank=True
    )
    total_buy = models.CharField(_("Total Buy"), max_length=255, null=True, blank=True)
    total_sell = models.CharField(
        _("Total Sell"), max_length=255, null=True, blank=True
    )
    profit = models.CharField(_("Profit"), max_length=255, null=True, blank=True)
