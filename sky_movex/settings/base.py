import os
import json
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# reading .env file
environ.Env.read_env(env_file=os.path.join(BASE_DIR, '.env'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

EMAIL_HOST_USER = "skymovextest@gmail.com"
EMAIL_HOST_PASSWORD = "iwaihdilbqyntqdv"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_countries',
    'drf_yasg',
    'validate_email',
    'corsheaders',
    'phonenumber_field',
    'rest_framework',
    'rest_framework.authtoken',
    'accounts.apps.AccountsConfig',
    'institute.apps.InstituteConfig',
    'home.apps.HomeConfig',
    'form.apps.FormConfig',
    'django_rest_passwordreset',
    'tinymce',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

WAGTAIL_SITE_NAME = 'My Example Site'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'sky_movex.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',

    ],
}

WSGI_APPLICATION = 'sky_movex.wsgi.application'

AUTH_USER_MODEL = 'accounts.User'

DEFAULT_AUTO_FIELD='django.db.models.AutoField' 

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
env.db()
DATABASES = {
    'default': env.db(),
    'extra': env.db('SQLITE_URL', default='sqlite:////tmp/my-tmp-sqlite.db')
}
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },

]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

# LANGUAGE_CODE = 'fa'
#
# TIME_ZONE = 'Asia/Tehran'
#
# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = True

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# add fonts and plugins to tiny mce
TINYMCE_DEFAULT_CONFIG = {
    "toolbar": "numlist bullist",
    'plugins': "paste,searchreplace,code,link,emoticons,image,imagetools,media,advlist lists",
    "font_formats": "B Nazanin;" +
                    "Arial;" +
                    "Tahoma;" +
                    "Times New Roman;",
    "selector": "textarea",
}

LOGGING = {
    'version': 1, 'disable_existing_loggers': False, 'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {'
                      'thread:d} {message}', 'style': '{',
        },
    },
    'filters': {'require_debug_true': {'()': 'django.utils.log.RequireDebugTrue', }, },
    'handlers': {
        'console': {
            'level': 'DEBUG', 'filters': ['require_debug_true'], 'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {'level': 'WARNING', 'class': 'logging.FileHandler', 'filename': 'Django.log', },
    },
    'loggers': {
        'django': {'handlers': ['console', 'file'], 'propagate': True, },
        # 'django.request': {
        #     'handlers': ['mail_admins'],
        #     'level': 'ERROR',
        #     'propagate': False,
        # },
    },
}
