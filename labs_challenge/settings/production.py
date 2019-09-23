import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from labs_challenge.settings.base import *
import os


DEBUG = False

# Fix MySQL Emoji support
DATABASES['default']['OPTIONS'] = {'charset': 'utf8mb4'}

# Honour the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow production host headers
ALLOWED_HOSTS = ['labs.walthome.duckdns.org']
