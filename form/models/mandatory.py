from django.db import models
from django.utils.translation import ugettext_lazy as _


class Mandatory(models.Model):
    SELL = "sell"
    BUY = "buy"

    ACCTIVITY_TYPE_CHOICES = ((SELL, _("Sell")), (BUY, _("Buy")))

    activity_type = models.CharField(
        _("Agency"), max_length=255, choices=ACCTIVITY_TYPE_CHOICES, default=BUY
    )
    agency = models.CharField(_("Agency"), max_length=255, null=True, blank=True)
    carrier = models.CharField(_("Carrier"), max_length=255, null=True, blank=True)
    airfreight = models.CharField(
        _("Airfreight"), max_length=255, null=True, blank=True
    )
    airway_bill = models.CharField(
        _("Airway Bill"), max_length=255, null=True, blank=True
    )
    pick_up = models.CharField(_("Pick up"), max_length=255, null=True, blank=True)
    customs = models.CharField(_("Customs "), max_length=255, null=True, blank=True)
    sbl = models.CharField(_("SBL"), max_length=255, null=True, blank=True)
    other_charge = models.CharField(
        _("Other Charge"), max_length=255, null=True, blank=True
    )
