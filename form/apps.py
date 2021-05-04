from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class FormConfig(AppConfig):
    name = "form"
    verbose_name = ugettext_lazy("Form")
