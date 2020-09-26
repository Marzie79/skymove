from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class HomeConfig(AppConfig):
    name = 'home'
    verbose_name = ugettext_lazy('Home')
