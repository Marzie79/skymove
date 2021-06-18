from django.db import models
from django.utils.translation import ugettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField


class Consignee(models.Model):
    SELLER = "seller"
    BUYER = "buyer"
    CONSIGNEE_TYPE = ((SELLER, "Seller"), (BUYER, "Buyer"))
    consignee_type = models.CharField(
        max_length=255, choices=CONSIGNEE_TYPE, null=True, blank=True
    )
    is_deleted = models.BooleanField(_("Is Deleted"), default=False)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    name = models.CharField(_("Name"), max_length=250, null=True, blank=True, unique=True)
    address = models.TextField(_("Address"), null=True, blank=True)
    email = models.EmailField(_("Email"), null=True, blank=True)
    phone_number = PhoneNumberField(
        verbose_name=_("Phone number"),
        help_text=_("Enter phone number with country code like : +98... "),
    )
