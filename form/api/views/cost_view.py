from form.api.serializers.cost_serializer import CostSerializer
from rest_framework import status
from rest_framework import permissions, viewsets, mixins
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from form.api.serializers import *
from form.models import *
from django.db import models as django_models
from rest_framework import filters


class CostView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = CostSerializer
    queryset = Cost.objects.all()
    permission_classes = (AllowAny,)


    def list(self, request, *args, **kwargs):
        if request.GET.get("create_date"):
            queryset = self.filter_queryset(self.get_queryset().filter(create_date__gt=request.GET.get("create_date")))
        elif request.GET.get("date"):
            queryset = self.filter_queryset(self.get_queryset().filter(date__gt=request.GET.get("date")))
        elif request.GET.get("invoice"):
            queryset = self.filter_queryset(self.get_queryset().filter(invoice__contains=request.GET.get("invoice")))
        elif request.GET.get("company"):
            queryset = self.filter_queryset(self.get_queryset().filter(company__contains=request.GET.get("company")))
        else:
            queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)