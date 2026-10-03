# Web Mapping course environment
# Python 3.12 + the GIS system libraries GeoDjango needs (GDAL, GEOS, PROJ, SpatiaLite).
# Installing them here means no student ever has to install GDAL on their own laptop.
FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends \
        binutils \
        gdal-bin \
        libgdal-dev \
        libgeos-dev \
        libproj-dev \
        libsqlite3-mod-spatialite \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
