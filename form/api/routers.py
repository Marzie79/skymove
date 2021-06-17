from form.models.statement import Statement
from form.api.views.courier_view import CourierView
from .views import *
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("shipment", ShipmentView)
router.register("courier", CourierView)
router.register("consignee", ConsigneeView)
router.register("statement", StatementView, "test")


urlpatterns = router.urls
