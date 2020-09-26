from rest_framework import generics, permissions, status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response
from institute.serializers import *
from institute.models import *


class Contact_Us(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def get_serializer_class(self):
        if self.action == 'create':
            return ContactSerializer
        else:
            return SupportSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            last_obj = Support.objects.latest('date')
            serialize = SupportSerializer(last_obj)
            return Response(serialize.data)
        except Support.DoesNotExist:
            return Response({})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(status=status.HTTP_201_CREATED, data={'message': 'the message is saved'})


# class LargeResultsSetPagination(PageNumberPagination):
#     page_size = 1


class News_List(generics.ListAPIView):
    serializer_class = NewsSerializer
    permission_classes = (permissions.AllowAny,)
    # pagination_class = LargeResultsSetPagination
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


class Services_List(generics.ListAPIView):
    serializer_class = ServiceSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Service.objects.all()


class One_Service(generics.RetrieveAPIView):
    serializer_class = ServiceSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Service.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.counter = instance.counter + 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class Most_Viewed(generics.ListAPIView):
    serializer_class = NewsSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = News.objects.all().order_by('-counter', '-date')[:4]


class Home_News(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = NewsSerializer
    queryset = News.objects.all().order_by('-date')[:4]


class A_Bout_Us(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ABoutUsSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            last_obj = ABoutUs.objects.latest('date')
            serializer = ABoutUsSerializer(last_obj)
            return Response(serializer.data)
        except ABoutUs.DoesNotExist:
            return Response({})
