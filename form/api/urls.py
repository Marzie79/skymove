from django.urls import path
from form.api.views import *

urlpatterns = [
    path("create/", ShipmentView.as_view()),
]
