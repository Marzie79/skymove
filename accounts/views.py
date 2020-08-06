from django.contrib.auth.decorators import login_required
from rest_framework import generics, permissions, status
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from rest_framework import authentication
from django.contrib import auth
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from accounts.serializers import *


class SignUp(generics.CreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.AllowAny,)


@permission_classes((AllowAny,))
class SignIn(APIView):
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def post(self, request):
        if request.data['email']:
            try:
                user = User.objects.get(email=request.data['email'])
            except User.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            user_set = authenticate(
                email=request.data['email'], password=request.data['password'])
            if user_set is not None:
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

