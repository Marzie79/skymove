from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseForm(models.Model):
    USD = "usd"
    EUR = "eur"
    TRY = "try"
    CURRENCY_STATUS = ((USD, "usd"), (EUR, "eur"), (TRY, "try"))
    date = models.DateField(_("Date"), blank=False, null=False)
    consignee = models.ForeignKey(
        "form.Consignee", null=True, blank=True, on_delete=models.SET_NULL
    )
    company_invoice_no = models.CharField(
        _("Company Invoice No"), max_length=255, null=True, blank=True
    )
    consignee_order_no = models.CharField(
        _("Consignee Order No"), max_length=255, null=True, blank=True
    )
    sender = models.CharField(_("Sender"), max_length=255, null=True, blank=True)
    receiver = models.CharField(_("Receiver"), max_length=255, null=True, blank=True)
    currency = models.CharField(
        _("Currency"), max_length=255, null=True, blank=True, choices=CURRENCY_STATUS
    )
    AWB_no_first = models.IntegerField(_("AWB No First"), null=True, blank=True)
    AWB_no_second = models.IntegerField(_("AWB No Second"), null=True, blank=True)
    from_in_base = models.CharField(_("From"), max_length=255, null=True, blank=True)
    to = models.CharField(_("To"), max_length=255, null=True, blank=True)
    via = models.CharField(_("Via"), max_length=255, null=True, blank=True)
    chargeable_weight = models.IntegerField(
        _("Chargeable Weight"), null=True, blank=True
    )
    gross_weight = models.IntegerField(_("Gross Weight"), null=True, blank=True)

    def save(self, *args, **kwargs):
        if (
            self.company_invoice_no
            or self.consignee_order_no
            or self.AWB_no_first
            or self.AWB_no_second
            or self.chargeable_weight
            or self.gross_weight
        ):
            super(BaseForm, self).save(*args, **kwargs)
