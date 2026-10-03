"""
Django settings for the DJwebmaps project (Django 5.2 LTS).
Set up for GitHub Codespaces and for local VS Code dev containers.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Development-only settings. Never use this key or DEBUG=True on a public server.
SECRET_KEY = "django-insecure-webmaps-classroom-key-change-before-deploying"
DEBUG = True

# Codespaces serves your site at https://<codespace-name>-8000.app.github.dev
ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".app.github.dev"]
# Needed so logins and forms (including the admin site) work through Codespaces.
CSRF_TRUSTED_ORIGINS = [
    "https://*.app.github.dev",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

INSTALLED_APPS = [
    "app",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "DJwebmaps.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "app.context_processors.map_keys",
            ],
        },
    },
]

WSGI_APPLICATION = "DJwebmaps.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/New_York"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ArcGIS access token. Students store it as a Codespaces secret named
# ARCGIS_API_KEY (or in a local .env) so it never gets committed to GitHub.
ARCGIS_API_KEY = os.environ.get("ARCGIS_API_KEY", "")
