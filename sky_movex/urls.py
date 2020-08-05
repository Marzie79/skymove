from django.contrib import admin
from django.urls import path
from accounts.views import SignUp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUp.as_view(), name='signup'),
]
