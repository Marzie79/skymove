from django.urls import path

from accounts.views import *

urlpatterns = [
    # path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('swagger.yaml/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('signup/', Sign_up.as_view(), name='sign_up'),
    path('login/', Log_in.as_view(), name='log_in'),
    path('validate_email/', Validate_Email.as_view(), name='validate_email'),
    path('edit_profile/', Edit_Profile.as_view({'post': 'update'}), name='edit'),
    path('contact_us/', Contact_Us.as_view(), name='contact_us'),

    ]
