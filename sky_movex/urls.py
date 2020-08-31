from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from accounts.views import *
from django.conf import settings
from django.conf.urls.static import static
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

schema_view = get_schema_view(
    openapi.Info(
        title="accounts API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('accounts/', include('accounts.urls')),
                  path('institute/', include('institute.urls')),
                  path('password_reset/confirm/', reset_password_confirm, name="reset-password-confirm"),
                  path('password_reset/', reset_password_request_token, name="reset-password-request"),
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
