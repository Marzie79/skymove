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
    active = models.BooleanField(verbose_name=_("Active"), default=True,
                                 help_text="if you set this field true this video is shown in home page")

    class Meta:
        ordering = ['-id']
        verbose_name = _("Video")
        verbose_name_plural = _("Video in home")

    def clean(self):
        if self.active:
            objs = HomeVideo.objects.filter(active=True)
            if self.pk:
                objs = objs.exclude(pk=self.pk)
            if objs.exists():
                objs.update(active=False)


class ABoutUsHome(models.Model):
    title = FarsiCharField(verbose_name=_("Title"), max_length=50)
    description = tinymce_models.HTMLField(verbose_name=_("Description"))
    active = models.BooleanField(verbose_name=_("Active"), default=True,
                                 help_text="if you set this field true this information is shown in about us in home page")

    class Meta:
        ordering = ['-id']
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
    phone_number = PhoneNumberField(verbose_name=_("Phone number"),
                                    help_text="enter phone number with country code like : +98... ")
    email = models.EmailField(verbose_name=_("Email"), validators=[validate_email], max_length=255)
    whats_app_phone_number = PhoneNumberField(verbose_name=_("Whats app phone number"), null=True, blank=True,
                                              help_text="enter phone number with country code like : +98... ")
    twitter = models.URLField(verbose_name=_("twitter"), null=True, blank=True)
    instagram = models.URLField(verbose_name=_("Instagram"), null=True, blank=True)
    medium = models.URLField(verbose_name=_("Medium"), null=True, blank=True)
    telegram = models.URLField(verbose_name=_("Telegram"), null=True, blank=True)
    facebook = models.URLField(verbose_name=_("Facebook"), null=True, blank=True)
    active = models.BooleanField(verbose_name=_("Active"), default=True,
                                 help_text="if you set this field true this information is shown in footer of pages")

    class Meta:
        ordering = ['-id']
        verbose_name = _("Social network")
        verbose_name_plural = _("Social networks in footer")

    def clean(self):
        if self.active:
            objs = SocialNetwork.objects.filter(active=True)
            if self.pk:
                objs = objs.exclude(pk=self.pk)
            if objs.exists():
                objs.update(active=False)
