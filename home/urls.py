from django.urls import path
from home.views import *

urlpatterns = [
    path('news-letter/', News_Letter.as_view()),
    path('home-video/', Home_video.as_view()),
    path('a-bout-us-home/', A_Bout_Us_Home.as_view()),
    path('social-network/', Social_Networks.as_view()),
]
