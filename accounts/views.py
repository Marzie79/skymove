from rest_framework import generics, permissions
from django.contrib.auth import authenticate
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import *
from accounts.serializers import ProfileSerializer
from rest_framework.authtoken.models import Token
from django.utils.crypto import get_random_string
from accounts.util import sending_email


class Sign_up(generics.CreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.AllowAny,)


class Sign_in(APIView):
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        if request.data['email']:
            try:
                user = User.objects.get(email=request.data['email'])

            except User.DoesNotExist:
                # if the email isn't valid in database response 404
                return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'email is not exist'})

            user_set = authenticate(email=request.data['email'], password=request.data['password'])
            if user.is_validate:
                if user_set is not None:
                    # everything is ok then response 200
                    token, created = Token.objects.get_or_create(user=user)
                    return Response(status=status.HTTP_200_OK,
                                    data={'message': 'user login', 'token': token.key})
                else:
                    # if password for that existing email isn't correct response 406
                    return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={'message': 'password is not correct'})
            else:
                # if user doesn't validate email
                return Response(status=status.HTTP_401_UNAUTHORIZED,
                                data={'email': request.data['email'], 'message': 'user should validate email'})
        else:
            # email doesn't exist in request
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'request is not correct'})


class Validate_Email(APIView):
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        if 'email' in request.data.keys():
            if 'validation' in request.data.keys():
                try:
                    user = User.objects.get(email=request.data['email'])

                    if user.is_validate:
                        return Response(status=status.HTTP_409_CONFLICT, data={'message': 'user is validate now'})

                    if user.validation == request.data['validation']:
                        user.is_validate = True
                        user.save()
                    else:
                        return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={'message': 'code is not correct'})

                    return Response(status=status.HTTP_200_OK, data={'message': 'email is validate'})

                except User.DoesNotExist:
                    # if the email isn't valid in database response 404
                    return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'email is not exist'})
            else:
                try:
                    user = User.objects.get(email=request.data['email'])

                    if user.is_validate:
                        return Response(status=status.HTTP_409_CONFLICT, data={'message': 'user is validate now'})

                    user.validation = get_random_string(length=6)
                    user.save()
                    message = sending_email(user.validation, user.email, 'sender_email', 'sender_password')

                    if message is not None:
                        return Response(status=status.HTTP_404_NOT_FOUND,
                                        data={'message': 'server has error try again'})

                    return Response(status=status.HTTP_200_OK, data={'message': 'sending email to user is successful',
                                                                     'email': request.data['email']})
                except User.DoesNotExist:
                    # if the email isn't valid in database response 404
                    return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'email is not exist'})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'email field is required'})
