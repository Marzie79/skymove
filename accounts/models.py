from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import validate_email
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from accounts.manager import UserManager
from utils.custom_fields import FarsiCharField


class User(AbstractBaseUser, PermissionsMixin):
    nationality = CountryField(verbose_name=_("Nationality"), max_length=2, blank_label='(select country)', default='IR')
    first_name = FarsiCharField(verbose_name=_("First name"), max_length=30,)
    # first_name_fa = FarsiCharField(verbose_name=_("First name Persian"), max_length=30, null=True, blank=True)
    last_name = FarsiCharField(verbose_name=_("Last name"), max_length=30)
    # last_name_fa = FarsiCharField(verbose_name=_("Last name"), max_length=30, null=True, blank=True)
    email = models.EmailField(verbose_name=_("Email"), validators=[validate_email], max_length=255, unique=True)
    email_2 = models.EmailField(verbose_name=_("Email 2"), validators=[validate_email], max_length=255,
                                unique=True, blank=True, null=True)
    phone_number = PhoneNumberField(verbose_name=_("Phone number"),
                                    help_text=_("Enter phone number with country code like : +98... "))
    company_name = FarsiCharField(verbose_name=_("Company name"), max_length=40, null=True, blank=True)

    validation = models.CharField(verbose_name=_("Validation"), max_length=6, null=True, blank=True)
    is_validate = models.BooleanField(verbose_name=_("Is validate"), default=False,
                                      help_text=_("If a user's email is validate select this item if this item is not selected user should validate her/his email with verification email."))
    is_active = models.BooleanField(verbose_name=_("Is active"), default=True, help_text=_("A user with out this item can't use site features."))
    is_admin = models.BooleanField(verbose_name=_("Is admin"), default=False)

    class Meta:
        ordering = ['-id']
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    objects = UserManager()

    # a field that we use for making any user unique in our database
    USERNAME_FIELD = 'email'

    # any field that we need them to get in creating superuser
    # we shouldn't use password and username in it because program get it automatically
    REQUIRED_FIELDS = ['nationality', 'first_name', 'last_name', 'phone_number']

    # we need four method of bottom for going to admin page
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
