from rest_framework import status
from rest_framework import permissions, viewsets, mixins
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from form.api.serializers import *
from form.models import *


class ShipmentView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()
    permission_classes = (AllowAny,)


    def create(self, validated_data):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


#
