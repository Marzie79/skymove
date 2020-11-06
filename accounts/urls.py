from django.urls import path
from accounts.views import *
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

urlpatterns = [
    path('signup/', Sign_up.as_view(), name='sign_up'),
    path('signin/', Log_in.as_view(), name='log_in'),
    path('validate-email/', Validate_Send_Email.as_view(), name='validate_email'),
    path('validate-email-code/', Validate_Send_code.as_view(), name='validate_email_code'),
    path('edit-profile/', Edit_Profile.as_view({'post': 'update'}), name='edit'),
    path('password-reset/confirm/', reset_password_confirm, name="reset-password-confirm"),
    path('password-reset/', reset_password_request_token, name="reset-password-request"),
    ]
