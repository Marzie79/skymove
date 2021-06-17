from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from form.api.serializers import *
from form.models import *


class ConsigneeView(viewsets.ModelViewSet):
    serializer_class = ConsigneeSerializer
    queryset = Consignee.objects.all()
    permission_classes = (AllowAny,)



#
