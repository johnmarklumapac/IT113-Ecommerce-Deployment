import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.base')
application = get_wsgi_application()

settings.ROOT_URLCONF = 'core.urls'
application = WhiteNoise(application)
