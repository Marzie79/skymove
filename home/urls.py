from django.urls import path
from home.views import *

urlpatterns = [
    path('news_letter/', News_Letter.as_view()),
    path('home_video/', Home_video.as_view()),
    path('a_bout_us_home/', A_Bout_Us_Home.as_view()),
]
