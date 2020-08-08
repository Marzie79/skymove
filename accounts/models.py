from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from accounts.manager import UserManager
from utils.custom_fields import FarsiCharField


class User(AbstractBaseUser):
    nationality = models.CharField(max_length=10, unique=True, error_messages={
        'unique': '600'})
    first_name = FarsiCharField(max_length=30)
    last_name = FarsiCharField(max_length=30)
    email = models.EmailField(max_length=255, unique=True, error_messages={
        'unique': '601'})
    phone_number = models.CharField(max_length=11)
    company_name = FarsiCharField(max_length=40, null=True, blank=True)
    validation = models.CharField(max_length=6, null=True, blank=True)
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
