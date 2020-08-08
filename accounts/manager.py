from django.contrib.auth.models import BaseUserManager
from accounts.util import random_generator


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.validation = random_generator()
        # set an algorithm to not show password directely
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
