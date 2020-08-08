from rest_framework import generics, permissions
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import *
from accounts.serializers import ProfileSerializer


class Sign_up(generics.CreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.AllowAny,)


@permission_classes((AllowAny,))
class Sign_in(APIView):
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def post(self, request):
        # email should have a value
        if request.data['email']:
            try:
                user = User.objects.get(email=request.data['email'])
            except User.DoesNotExist:
                # if the email isn't valid in database response 404
                return Response(status=status.HTTP_404_NOT_FOUND)
            user_set = authenticate(
                email=request.data['email'], password=request.data['password'])
            if user.is_active:
                if user_set is not None:
                    login(request, user)
                    # everything is ok then response 200
                    return Response(status=status.HTTP_200_OK)
                else:
                    # if password for that existing email isn't correct response 406
                    return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                # if user doesn't validate email
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            # email doesn't exist in request
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Log_out(APIView):
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
