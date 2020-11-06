from .views import *
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('news', NewsViewSet)
router.register('services', ServicesViewSet)
router.register('contact-us', ContactusViewSet, basename='Contactus')

urlpatterns = [
    path('most-viewed/', Most_Viewed.as_view(), name='most_viewed'),
    path('home-news/', Home_News.as_view(), name='home_news'),
    path('a-bout-us/', A_Bout_Us.as_view(), name='a_bout_us'),
]

urlpatterns += router.urls
