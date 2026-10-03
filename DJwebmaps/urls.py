"""
Definition of urls for DJwebmaps.
"""

from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("admin/", admin.site.urls),
]
