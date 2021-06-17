from rest_framework import viewsets
from form.api.serializers import *
from form.models import *


class ConsigneeView(viewsets.ModelViewSet):
    serializer_class = ConsigneeSerializer
    queryset = Consignee.objects.all()


#
