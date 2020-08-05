from django.contrib.auth.models import BaseUserManager
from accounts.util import random_generator


class UserManager(BaseUserManager):
    # def create_user(self, email, nationality, first_name, last_name, phone_number, company_name=None,
    #                 password=None, validation=None):
    #     if not (email or nationality or first_name or last_name or phone_number):
    #         raise ValueError('an error has occurred')
    # user = self.model(
    #     email=self.normalize_email(email).lower(),
    #     nationality=nationality,
    #     first_name=first_name,
    #     last_name=last_name,
    #     phone_number=phone_number,
    #     company_name=company_name,
    #     validation=random_generator(),
    # )
    def create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.validation = random_generator()
        user.set_password(password)
        user.save(using=self._db)
        return user

    # fields that we want get it from user when we want to create superuser
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(
            email=email,
            password=password,
            **extra_fields,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user
