from django.contrib import admin
from form.models import *
from django.shortcuts import redirect

# Register your models here.
admin.sites.site.register(Courier)
admin.sites.site.register(Shipment)
admin.sites.site.register(Mandatory)
admin.sites.site.register(Optional)
admin.sites.site.register(BaseFormCourier)
admin.sites.site.register(BaseForm)
admin.sites.site.register(SellBuyCourier)


# @admin.register(Shipment)
# class ShipmentAdmin(admin.ModelAdmin):
#     def change_view(self, request, object_id, form_url="", extra_context=None):
#         return redirect("https://google.com")
