from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class AccountsConfig(AppConfig):
    name = 'accounts'
    verbose_name = ugettext_lazy('accounts')

    def ready(self):
        import accounts.signals
