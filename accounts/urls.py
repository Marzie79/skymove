from django.urls import path
from accounts.views import *
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm


urlpatterns = [
    # path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('swagger.yaml/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('signup/', Sign_up.as_view(), name='sign_up'),
    path('signin/', Log_in.as_view(), name='log_in'),
    path('validate_email/', Validate_Send_Email.as_view(), name='validate_email'),
    path('validate_email_code/', Validate_Send_code.as_view(), name='validate_email_code'),
    path('edit_profile/', Edit_Profile.as_view({'post': 'update'}), name='edit'),
    path('password_reset/confirm/', reset_password_confirm, name="reset-password-confirm"),
    path('password_reset/', reset_password_request_token, name="reset-password-request"),
    ]
