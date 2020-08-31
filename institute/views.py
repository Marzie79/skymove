from rest_framework import generics, permissions, status
from rest_framework.response import Response
from institute.serializers import *
from institute.models import *


class Contact_Us(generics.CreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(status=status.HTTP_201_CREATED, data={'message': 'the message is saved'})


class News_List(generics.ListAPIView):
    serializer_class = NewsSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = News.objects.all()


class One_News(generics.RetrieveAPIView):
    serializer_class = NewsSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = News.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.counter = instance.counter + 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)