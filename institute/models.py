from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import validate_email
from phonenumber_field.modelfields import PhoneNumberField
from utils.custom_fields import FarsiCharField
from tinymce import models as tinymce_models


class Contact(models.Model):
    name = FarsiCharField(verbose_name=_("Name"), max_length=60)
    email = models.EmailField(verbose_name=_("Email"), validators=[validate_email], max_length=255)
    phone_number = PhoneNumberField(verbose_name=_("Phone number"), )
    message = models.TextField(verbose_name=_("Message"), )

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")


class News(models.Model):
    title = FarsiCharField(verbose_name=_("Title"), max_length=50)
    description = tinymce_models.HTMLField(verbose_name=_("Description"))
    image = models.ImageField(verbose_name=_("Image"), upload_to='news/')
    date = models.DateTimeField(verbose_name=_("Date"), auto_now_add=True)
    counter = models.IntegerField(verbose_name=_("Counter"), default=0)

    class Meta:
        ordering = ['-date']
        verbose_name = _("News")
        verbose_name_plural = _("AllNews")


class Support(models.Model):
    email = models.EmailField(verbose_name=_("Email"), validators=[validate_email], max_length=255)
    phone_number = PhoneNumberField(verbose_name=_("Phone number"), )
    date = models.DateTimeField(verbose_name=_("Date"), auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = _("Support")
        verbose_name_plural = _("AllSupport")


class Service(models.Model):
    title = FarsiCharField(verbose_name=_("Title"), max_length=50)
    description = tinymce_models.HTMLField(verbose_name=_("Description"))
    image = models.ImageField(verbose_name=_("Image"), upload_to='service/')
    counter = models.IntegerField(verbose_name=_("Counter"), default=0)

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")
