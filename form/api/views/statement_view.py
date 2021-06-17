from django.db.models.aggregates import Max
from rest_framework import status
from rest_framework import permissions, viewsets, mixins
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from form.api.serializers import *
from form.models import *


class StatementView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = Statement
    permission_classes = (AllowAny,)
    queryset = Statement.objects.all()
    lookup_fields = ["consignee", "currency"]

    def get_serializer_class(self):
        if self.action == 'create':
            return StatemnetCreateSerializer

    def list(self, request, *args, **kwargs):
        consignee_name = self.request.GET.get("consignee")
        currency = self.request.GET.get("currency")

        consignee = Consignee.objects.filter(name=consignee_name)

        if consignee.exists():
            statements = Statement.objects.filter(shipment__consignee__name=consignee_name, consignee__name=consignee_name, currency=currency)
            shipments = Shipment.objects.filter(base_form__consignee=consignee.first(), base_form__currency=currency).exclude(pk__in=statements.values_list("shipment__id",flat=True)).order_by("-base_form__date")
            statements_courier = Statement.objects.filter(courier__consignee=consignee, courier__base_form__currency=currency, consignee__name=consignee_name)
            courier = Courier.objects.filter(base_form_courier__consignee=consignee.first(), currency=currency).exclude(pk__in=statements_courier.values_list("courier__id",flat=True)).order_by("-base_form_courier__date")
            max = Max(len(shipments), len(courier))
            for item in range(0,max):
                if shipments or courier:
                    if (shipments and courier and shipments.first().base_form.date > courier.base_form_courier.date) or (shipments and not courier):
                        obj = Statement()
                        obj.currency = shipments.first().base_form.currency
                        obj.shipment = shipments.first()
                        last = Statement.objects.all().order_by("-order").first()
                        obj.balance = (last.balance + shipments.first().total_sell) - (last.charge if last.charge else 0)
                        shipments = shipments.exclude(shipments.first())
                    else:
                        obj = Statement()
                        obj.currency = courier.first().base_form.currency
                        obj.courier = courier.first()
                        last = Statement.objects.all().order_by("-order").first()
                        obj.balance = (last.balance + courier.first().total_buy) - (last.charge if last.charge else 0)
                        obj.order = Statement.objects.all().order_by("-order").first() + 1
                        courier = courier.exclude(courier.first())
                    obj.save()

        need_obj = Statement.objects.filter(consignee__name=consignee_name, currency=currency)

        data_list = []

        for item in need_obj:
            date = item.date
            if not date:
                if item.shipment:
                    date = item.shipment.date
                else:
                    date = item.courier.date
            invoice_no = ""
            if not invoice_no:
                if item.shipment:
                    invoice_no = item.shipment.base_form.company_invoice_no
                else:
                    invoice_no = item.courier.base_form_courier.company_invoice_no
            consignee_order_no = ""
            if not consignee_order_no:
                if item.shipment:
                    consignee_order_no = item.shipment.base_form.consignee_order_no
                else:
                    consignee_order_no = item.courier.base_form_courier.consignee_order_no
            credit = ""
            if not credit:
                if item.shipment:
                    credit = item.shipment.total_sell
                else:
                    credit = item.courier.total_buy

            my_obj = {"date": date,
            "invoice_no": invoice_no,
            "refrence_no": consignee_order_no,
            "credit": credit,
            "charge": item.charge,
            "balance": item.balance
             }

            data_list.append(my_obj)


        return Response({"date":data_list})