from .views import *
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("shipment", ShipmentView)

urlpatterns = router.urls
