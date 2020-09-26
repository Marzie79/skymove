from django.urls import path
from institute.views import *

urlpatterns = [
    path('contact_us/', Contact_Us.as_view({'get': 'retrieve', 'post': 'create'}), name='contact_us'),
    path('news/', News_List.as_view(), name='news'),
    path('a_bout_us/', A_Bout_Us.as_view(), name='a_bout_us'),
    path('news/<int:pk>/', One_News.as_view(), name='one_news'),
    path('services/', Services_List.as_view(), name='services'),
    path('service/<int:pk>/', One_Service.as_view(), name='one_service'),
    path('most_viewed/', Most_Viewed.as_view(), name='most_viewed'),
    path('home_news/', Home_News.as_view(), name='home_news'),
]
