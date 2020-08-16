from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
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


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
