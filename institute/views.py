from rest_framework import permissions, viewsets, generics, mixins
# from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from institute.serializers import *
from institute.models import *


class ContactusViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny,)
    lookup_value_regex = '[0-8a-f]{32}'

    def get_queryset(self):
        if self.action == 'create':
            return ContactUs.objects.all()
        else:
            return Support.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ContactSerializer
        else:
            return SupportSerializer

    def list(self, request, *args, **kwargs):
        try:
            last_obj = Support.objects.filter(active=True).last()
            if not last_obj:
                last_obj = Support.objects.latest('id')
                serialize = SupportSerializer(last_obj)
            else:
                serialize = SupportSerializer(last_obj)
            return Response(serialize.data)
        except Support.DoesNotExist:
            return Response({})


# class LargeResultsSetPagination(PageNumberPagination):
# page_size = 1


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NewsSerializer
    permission_classes = (permissions.AllowAny,)
    # pagination_class = LargeResultsSetPagination
    queryset = News.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.counter = instance.counter + 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ServicesViewSet(viewsets.ReadOnlyModelViewSet):
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


class A_Bout_Us(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ABoutUsSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            last_obj = ABoutUs.objects.filter(active=True).last()
            if not last_obj:
                last_obj = ABoutUs.objects.latest('id')
                serializer = ABoutUsSerializer(last_obj, context={"request": request})
            else:
                serializer = ABoutUsSerializer(last_obj, context={"request": request})
            return Response(serializer.data)
        except ABoutUs.DoesNotExist:
            return Response({})


class Home_News(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = NewsSerializer
    queryset = News.objects.all().order_by('-date')[:4]
