from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from .util import sending_email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = reset_password_token.key
    sending_email(email_plaintext_message, 'skymovextest@gmail.com', 'skymovextest@gmail.com', '')

    # email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'),
    #                                                reset_password_token.key)
