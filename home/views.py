from rest_framework import generics, permissions
from rest_framework.response import Response
from home.serializers import *


class News_Letter(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = NewsLetterSerializer


class Home_video(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = HomeVideoSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            last_obj = HomeVideo.objects.filter(active=True)
            if not last_obj:
                last_obj = HomeVideo.objects.latest('id')
                serializer = HomeVideoSerializer(last_obj, context={"request": request})
            else:
                serializer = HomeVideoSerializer(last_obj[0], context={"request": request})
            return Response(serializer.data)
        except HomeVideo.DoesNotExist:
            return Response({})


class A_Bout_Us_Home(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ABoutUsHomeSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            last_obj = ABoutUsHome.objects.filter(active=True)
            if not last_obj:
                last_obj = ABoutUsHome.objects.latest('id')
                serializer = ABoutUsHomeSerializer(last_obj, context={"request": request})
            else:
                serializer = ABoutUsHomeSerializer(last_obj[0], context={"request": request})
            return Response(serializer.data)
        except ABoutUsHome.DoesNotExist:
            return Response({})


class Social_Networks(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SocialNetworkSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            last_obj = SocialNetwork.objects.filter(active=True)
            if not last_obj:
                last_obj = SocialNetwork.objects.latest('id')
                serializer = SocialNetworkSerializer(last_obj)
            else:
                serializer = SocialNetworkSerializer(last_obj[0])
            return Response(serializer.data)
        except SocialNetwork.DoesNotExist:
            return Response({})
