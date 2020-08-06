from django.contrib import admin
from django.urls import path
from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', SignIn.as_view(), name='exame')
]
