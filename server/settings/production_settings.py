import os
from settings.common_settings import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'OPTIONS': {
            'client_encoding': 'UTF8',
    },
    }
}

STATIC_URL = '/static/static/'
MEDIA_URL ='/static/media/'

STATIC_ROOT = '/vol/web/media'
MEDIA_ROOT = '/vol/web/static'
