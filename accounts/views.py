from django.contrib.auth import authenticate
from django.utils.crypto import get_random_string
from rest_framework import generics, permissions, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from accounts.enums import *
from accounts.serializers import *
from accounts.util import sending_email


class Sign_up(generics.CreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.AllowAny,)


class Log_in(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LogInSerializer

    def post(self, request):
        try:
            serializer = LogInSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = User.objects.get(email=serializer.data['email'])
        except User.DoesNotExist:
            # if the email isn't valid in database response 404
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'email is not exist'})

        user_set = authenticate(email=serializer.data['email'], password=serializer.data['password'])
        if user.is_validate:
            if user_set is not None:
                # everything is ok then response 200
                token, created = Token.objects.get_or_create(user=user)
                return Response(status=status.HTTP_200_OK, data={'token': token.key})
            else:
                # if password for that existing email isn't correct response 406
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                                data={'message': 'password is not correct'})
        else:
            # if user doesn't validate email
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data={
                                'email': serializer.data['email'], 'message': 'user should validate email'
                            })


class Validate_Send_Email(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = EmailAddressSerializer

    def post(self, request):
        try:
            serializer = EmailAddressSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            if request.user.is_authenticated:
                user = request.user
                user.email_2 = serializer.data['email']
                user.save()
            else:
                user = User.objects.get(email=serializer.data['email'])

            if user.is_validate and user.email_2 is None:
                return Response(status=status.HTTP_409_CONFLICT, data={'message': 'user is validate now'})

            user.validation = get_random_string(length=6)
            user.save()
            if request.user.is_authenticated:
                message = sending_email(user.validation, user.email_2, Email.EMAIL_ADDRESS.value, Email.PASSWORD.value)
            else:
                message = sending_email(user.validation, user.email, Email.EMAIL_ADDRESS.value,
                                        Email.PASSWORD.value)
            if message is not None:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                data={'message': 'server has error try again'})

            return Response(status=status.HTTP_200_OK, data={
                'message': 'sending email to user is successful',
                'email': request.data['email']
            })
        except User.DoesNotExist:
            # if the email isn't valid in database response 404
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'email is not exist'})


class Validate_Send_code(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ValidationCodeSerializer

    def post(self, request):
        try:
            serializer = ValidationCodeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serialize = serializer.data
            if serializer.data['email'] is '':
                serialize['email'] = User.objects.get(validation=serializer.data['validation']).email
            user = User.objects.get(email=serialize['email'])
            if user.is_validate and user.email_2 is None:
                return Response(status=status.HTTP_409_CONFLICT, data={'message': 'user is validate now'})

            if user.validation == serializer.data['validation']:
                if user.email_2 is not None:
                    user.email = user.email_2
                    user.email_2 = None

                user.is_validate = True
                user.validation = None
                user.save()
            else:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                                data={'message': 'code is not correct'})

            return Response(status=status.HTTP_200_OK, data={'message': 'email is validate'})

        except User.DoesNotExist:
            # if the email isn't valid in database response 404
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'email is not exist'})


class Edit_Profile(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (TokenAuthentication,)

    def update(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
