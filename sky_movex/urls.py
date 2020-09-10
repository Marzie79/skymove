from django.contrib import admin
from django.urls import include, path
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

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/accounts/', include(('accounts.urls', 'v2'), namespace='v2')),
                  # path('api/v1/accounts/', include(('accounts.urls', 'v1'), namespace='v1')),
                  path('api/v1/institute/', include(('institute.urls', 'v1'), namespace='v1')),
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
