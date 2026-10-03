"""
Makes map API keys available to every template as {{ ARCGIS_API_KEY }}.
"""

from django.conf import settings


def map_keys(request):
    return {"ARCGIS_API_KEY": settings.ARCGIS_API_KEY}
