from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import validate_email
from phonenumber_field.modelfields import PhoneNumberField
from utils.custom_fields import FarsiCharField
from tinymce import models as tinymce_models


class NewsLetter(models.Model):
    email = models.EmailField(verbose_name=_("Email"), validators=[validate_email], max_length=255, unique=True)

    class Meta:
        ordering = ['-id']
        verbose_name = _("News letter")
        verbose_name_plural = _("All news letter")


class HomeVideo(models.Model):
    video = models.FileField(upload_to='video_uploaded/')
    date = models.DateTimeField(verbose_name=_("Date"), auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = _("Video")
        verbose_name_plural = _("Video in home")


class ABoutUsHome(models.Model):
    title = FarsiCharField(verbose_name=_("Title"), max_length=50)
    description = tinymce_models.HTMLField(verbose_name=_("Description"))
    date = models.DateTimeField(verbose_name=_("Date"), auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = _("A bout us in home")
        verbose_name_plural = _("All a bout us in home")


class ABoutUsHomeSlideShow(models.Model):
    a_bout_us = models.ForeignKey(ABoutUsHome, verbose_name=_("Image"), on_delete=models.CASCADE,
                                  related_name='pictures')
    image = models.ImageField(verbose_name=_("Image"), upload_to='a_bout_us_home/')

    class Meta:
        ordering = ['-a_bout_us']
        verbose_name = _("Picture")
        verbose_name_plural = _("Pictures")

    def __str__(self):
        return self.image.name


class SocialNetwork(models.Model):
    phone_number = PhoneNumberField(verbose_name=_("Phone number"), )
    email = models.EmailField(verbose_name=_("Email"), validators=[validate_email], max_length=255)
    whats_app_phone_number = PhoneNumberField(verbose_name=_("Whats app phone number"), null=True, blank=True)
    twitter = models.URLField(verbose_name=_("twitter"), null=True, blank=True)
    instagram = models.URLField(verbose_name=_("Instagram"), null=True, blank=True)
    medium = models.URLField(verbose_name=_("Medium"), null=True, blank=True)
    telegram = models.URLField(verbose_name=_("Telegram"), null=True, blank=True)
    facebook = models.URLField(verbose_name=_("Facebook"), null=True, blank=True)

    class Meta:
        ordering = ['-id']
        verbose_name = _("Social network")
        verbose_name_plural = _("Social networks in footer")
