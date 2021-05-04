from django.contrib import admin
from form.models import *

# Register your models here.
admin.sites.site.register(BaseForm)
admin.sites.site.register(Optional)
admin.sites.site.register(Shipment)
