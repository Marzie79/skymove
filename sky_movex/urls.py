from django.contrib import admin
from django.urls import include, path
from django_rest_passwordreset.models import ResetPasswordToken
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from accounts.views import *
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        # version='v2',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

v1 = [
    path('accounts/', include('accounts.urls')),
    path('institute/', include('institute.urls')),
    path('home/', include('home.urls')),
]

urlpatterns = [
                  path('admin/', admin.site.urls, admin.site.unregister(ResetPasswordToken),
                       admin.site.unregister(Token)),
                  path('api/v1/', include((v1, 'v1'), namespace='v1')),
                  # path('api/v2/', include((v2, 'v2'), namespace='2')),
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
