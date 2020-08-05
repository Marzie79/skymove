from rest_framework import generics, permissions

from accounts.serializers import *


class SignUp(generics.CreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.AllowAny,)
