"""WSGI config for DJwebmaps."""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DJwebmaps.settings")
application = get_wsgi_application()
