from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseForm(models.Model):
    date = models.DateField(_("Date"), blank=False, null=False)
    Consignee = models.CharField(_("Consignee"), max_length=255, null=True, blank=True)
    company_invoice_no = models.CharField(
        _("Company Invoice No"), max_length=255, null=True, blank=True
    )
    consignee_order_no = models.CharField(
        _("Consignee Order No"), max_length=255, null=True, blank=True
    )
    sender = models.CharField(_("Sender"), max_length=255, null=True, blank=True)
    receiver = models.CharField(_("Receiver"), max_length=255, null=True, blank=True)
    currency = models.CharField(_("Currency"), max_length=255, null=True, blank=True)
    AWB_no_first = models.CharField(
        _("AWB No First"), max_length=255, null=True, blank=True
    )
    AWB_no_second = models.CharField(
        _("AWB No Second"), max_length=255, null=True, blank=True
    )
    from_in_base = models.CharField(_("From"), max_length=255, null=True, blank=True)
    to = models.CharField(_("To"), max_length=255, null=True, blank=True)
    via = models.CharField(_("Via"), max_length=255, null=True, blank=True)
    chargeable_weight = models.CharField(
        _("Chargeable Weight"), max_length=255, null=True, blank=True
    )
    gross_weight = models.CharField(
        _("Gross Weight"), max_length=255, null=True, blank=True
    )

    