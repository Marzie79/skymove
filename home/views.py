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
            last_obj = HomeVideo.objects.latest('date')
            serializer = HomeVideoSerializer(last_obj, context={"request": request})
            return Response(serializer.data)
        except HomeVideo.DoesNotExist:
            return Response({})


class A_Bout_Us_Home(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ABoutUsHomeSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            last_obj = ABoutUsHome.objects.latest('date')
            serializer = ABoutUsHomeSerializer(last_obj, context={"request": request})
            return Response(serializer.data)
        except ABoutUsHome.DoesNotExist:
            return Response({})
