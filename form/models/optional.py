from django.db import models
from django.utils.translation import ugettext_lazy as _


class Optional(models.Model):
    agency = models.CharField(_("Agency"), max_length=255, null=True, blank=True)
    carrier = models.CharField(_("Carrier"), max_length=255, null=True, blank=True)
    airfreight = models.CharField(
        _("Airfreight"), max_length=255, null=True, blank=True
    )
    airway_bill = models.CharField(
        _("Airway Bill"), max_length=255, null=True, blank=True
    )
    pick_up = models.CharField(_("Pick up"), max_length=255, null=True, blank=True)
    ordino = models.CharField(_("ordino"), max_length=255, null=True, blank=True)
    customs = models.CharField(_("Customs "), max_length=255, null=True, blank=True)
    warehouse_fee = models.CharField(
        _("Warehouse Fee"), max_length=255, null=True, blank=True
    )
    document_under_our_compnay_name = models.CharField(
        _("Document Under Our Compnay Name"), max_length=255, null=True, blank=True
    )
    other_charge = models.CharField(
        _("Other Charge"), max_length=255, null=True, blank=True
    )
