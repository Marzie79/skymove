from django.db import models
from django.utils.translation import ugettext_lazy as _


class SellBuyCourier(models.Model):
    ups_fee = models.IntegerField(_("UPS Fee"), null=True, blank=True)
    fuel_surcharge_ups = models.IntegerField(
        _("Fuel Surcharge UPS"), null=True, blank=True
    )
    fuel_surcharge_ups_percentage = models.CharField(
        _("Fuel Surcharge UPS Percentage"), null=True, blank=True, max_length=250
    )
    eph_ups_percentage = models.IntegerField(_("EPH UPS Percentage"), null=True, blank=True)
    eph_ups = models.IntegerField(_("EPH UPS"), null=True, blank=True)
    out_of_area_ups = models.IntegerField(_("Out Of Area UPS"), null=True, blank=True)
    dhl_fee = models.IntegerField(_("DHL Fee"), null=True, blank=True)
    fuel_surcharge_dhl = models.IntegerField(
        _("Fuel Surcharge DHL"), null=True, blank=True
    )
    fuel_surcharge_dhl_percentage = models.CharField(
        _("Fuel Surcharge DHL Percentage"), null=True, blank=True, max_length=250
    )
    eph_dhl = models.IntegerField(_("EPH DHL"), null=True, blank=True)
    out_of_area_dhl = models.IntegerField(_("Out Of Area DHL"), null=True, blank=True)
    aramex_fee = models.IntegerField(_("Aramex Fee"), null=True, blank=True)
    domestic_transfer_ups = models.IntegerField(
        _("Domestic Transfer UPS"), null=True, blank=True
    )
    eph_domestic = models.IntegerField(_("EPH Domestic"), null=True, blank=True)
    tax_for_domestic = models.IntegerField(_("TAX For Domestic"), null=True, blank=True)

    def save(self, *args, **kwargs):
        if (
            self.ups_fee
            or self.fuel_surcharge_ups
            or self.eph_ups
            or self.out_of_area_ups
            or self.dhl_fee
            or self.fuel_surcharge_dhl
            or self.eph_dhl
            or self.out_of_area_dhl
            or self.aramex_fee
            or self.domestic_transfer_ups
            or self.eph_domestic
            or self.tax_for_domestic
        ):
            super(SellBuyCourier, self).save(*args, **kwargs)
