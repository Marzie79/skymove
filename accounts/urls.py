from django.urls import path
from accounts.views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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
    # path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('swagger.yaml/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('signup/', Sign_up.as_view(), name='sign_up'),
    path('signin/', Sign_in.as_view(), name='sign_in'),
    path('validate_email/', Validate_Email.as_view(), name='validate_email'),
    path('edit_profile/', Edit_Profile.as_view({'post': 'update'}), name='edit'),
    path('contact_us/', Contact_Us.as_view(), name='contact_us'),

]
