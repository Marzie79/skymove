from django.urls import path
from accounts.views import *

urlpatterns = [
    path('signup/', Sign_up.as_view(), name='sign_up'),
    path('signin/', Sign_in.as_view(), name='sign_in'),
    path('logout/', Log_out.as_view(), name='log_out'),
]
