from django.db import models
from django.utils.translation import ugettext_lazy as _

from form.models import BaseFormCourier, SellBuyCourier


class Courier(models.Model):
    is_deleted = models.BooleanField(_("Is Deleted"), default=False)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    active = models.BooleanField(_("Active"), default=True)
    base_form_courier = models.ForeignKey(BaseFormCourier, on_delete=models.CASCADE)
    sell = models.ForeignKey(
        SellBuyCourier, on_delete=models.CASCADE, related_name="sell_form"
    )
    buy = models.ForeignKey(
        SellBuyCourier, on_delete=models.CASCADE, related_name="buy_form"
    )
    total_buy = models.IntegerField(_("Total Buy"), null=True, blank=True)
    total_sell = models.IntegerField(_("Total Sell"), null=True, blank=True)
    custom_clearnace_buy = models.IntegerField(
        _("Custom Clearnace Buy"), null=True, blank=True
    )
    custom_clearnace_sell = models.IntegerField(
        _("Custom Clearnace Sell"), null=True, blank=True
    )
    profit_sell = models.IntegerField(_("Profit Sell"), null=True, blank=True)
    profit = models.IntegerField(_("Profit"), null=True, blank=True)
