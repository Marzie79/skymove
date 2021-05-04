from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from form.api.serializers import *
from form.models import *


class ShipmentView(generics.CreateAPIView):
    serializer_class = ShipmentSerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (TokenAuthentication,)

    def create(self, validated_data):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
