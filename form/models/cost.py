from django.db import models
from django.utils.translation import ugettext_lazy as _


class Cost(models.Model):
    create_date = models.DateField(_("Date"), auto_now_add=True)
    date = models.DateField(_("Date"), blank=False, null=False)
    company_name = models.CharField(
        _("Company Name"), max_length=255, null=True, blank=True
    )
    description = models.CharField(
        _("Description"), max_length=255, null=True, blank=True
    )
    invoice = models.CharField(_("Invoice"), max_length=255, null=True, blank=True)
    deposit = models.CharField(_("Deposit"), null=True, blank=True, max_length=255)
    irr = models.CharField(_("IRR"), null=True, blank=True, max_length=255)
    try_value = models.CharField(_("TRY"), max_length=255, null=True, blank=True)
    usd = models.CharField(_("USD"), max_length=255, null=True, blank=True)
    xe = models.CharField(_("XE"), null=True, blank=True, max_length=255)
