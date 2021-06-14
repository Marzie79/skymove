from django.db import models
from django.utils.translation import ugettext_lazy as _


class Mandatory(models.Model):
    agency = models.CharField(_("Agency"), max_length=255, null=True, blank=True)
    carrier = models.CharField(_("Carrier"), max_length=255, null=True, blank=True)
    airfreight = models.IntegerField(_("Airfreight"), null=True, blank=True)
    airway_bill = models.IntegerField(_("Airway Bill"), null=True, blank=True)
    pick_up = models.IntegerField(_("Pick up"), null=True, blank=True)
    customs = models.IntegerField(_("Customs"), null=True, blank=True)
    sbl = models.IntegerField(_("SBL"), null=True, blank=True)
    other_charge = models.IntegerField(_("Other Charge"), null=True, blank=True)
    other_charge_second = models.IntegerField(_("Other Charge_second"), null=True, blank=True)
    other_charge_name = models.CharField(_("Other Charge Name"), max_length=255, null=True, blank=True)
    other_charge_second_name = models.CharField(_("Other Charge Name Second"), max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if (
            self.airfreight
            or self.airway_bill
            or self.pick_up
            or self.customs
            or self.sbl
            or self.other_charge
            or self.other_charge_second
        ):
            super(Mandatory, self).save(*args, **kwargs)
