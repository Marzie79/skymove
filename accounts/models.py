from django.core.validators import validate_email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from accounts.manager import UserManager
from phone_field import PhoneField
from utils.custom_fields import FarsiCharField
from django_countries.fields import CountryField


class User(AbstractBaseUser):
    nationality = CountryField(max_length=2, blank_label='(select country)')
    first_name = FarsiCharField(max_length=30)
    last_name = FarsiCharField(max_length=30)
    email = models.EmailField(validators=[validate_email], max_length=255, unique=True)
    email_2 = models.EmailField(validators=[validate_email], max_length=255, unique=True, blank=True, null=True)
    phone_number = PhoneField()
    company_name = FarsiCharField(max_length=40, null=True, blank=True)
    validation = models.CharField(max_length=6, null=True, blank=True)
    is_validate = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        ordering = ['nationality']

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


class Contact(models.Model):
    name = FarsiCharField(max_length=60)
    email = models.EmailField(validators=[validate_email], max_length=255)
    phone_number = PhoneField()
    message = models.TextField()
