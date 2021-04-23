from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class InstituteConfig(AppConfig):
    name = 'institute'
    verbose_name = ugettext_lazy('Institute')
