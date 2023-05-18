import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.base')
application = get_wsgi_application()
application = get_wsgi_application()

from django.conf import settings

settings.ROOT_URLCONF = 'core.urls'
