from django.urls import path
from institute.views import *

urlpatterns = [
    path('contact_us/', Contact_Us.as_view(), name='contact_us'),
    path('news/', News_List.as_view(), name='news'),
    path('news/<int:pk>/', One_News.as_view(), name='one_news'),
]
