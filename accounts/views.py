from accounts.serializers import *
from accounts.serializers import ProfileSerializer
from accounts.models import *
from accounts.util import sending_email
from rest_framework import generics, permissions, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.utils.crypto import get_random_string


class Sign_up(generics.CreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.AllowAny,)


class Sign_in(APIView):
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        if 'email' in request.data:
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
                    return Response(status=status.HTTP_200_OK, data={'token': token.key})
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
        if request.GET.get('valid'):
            try:
                user = User.objects.get(email=request.data['email'])
                if user.is_validate and user.email_2 is None:
                    return Response(status=status.HTTP_409_CONFLICT, data={'message': 'user is validate now'})

                if user.validation == request.data['validation']:
                    if user.email_2 is not None:
                        user.email = user.email_2
                        user.email_2 = None

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
                if request.user.is_authenticated:
                    user = request.user
                    user.email_2 = request.data['email']
                    user.save()
                else:
                    user = User.objects.get(email=request.data['email'])

                if user.is_validate and user.email_2 is None:
                    return Response(status=status.HTTP_409_CONFLICT, data={'message': 'user is validate now'})

                user.validation = get_random_string(length=6)
                user.save()
                if request.user.is_authenticated:
                    message = sending_email(user.validation, user.email_2, 'sender_email', 'sender_password')
                else:
                    message = sending_email(user.validation, user.email, 'sender_email', 'sender_password')
                # TODO: make it comment just for having test
                # if message is not None:
                #     return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                #                     data={'message': 'server has error try again'})

                return Response(status=status.HTTP_200_OK, data={'message': 'sending email to user is successful',
                                                                 'email': request.data['email']})
            except User.DoesNotExist:
                # if the email isn't valid in database response 404
                return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'email is not exist'})


class Edit_Profile(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def update(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class Contact_Us(generics.CreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(status=status.HTTP_201_CREATED, data={'message': 'the message is saved'})
