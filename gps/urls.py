#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from gps.view.index import  *

urlpatterns = [
    url('^getPeople/$', getPeople),
    url('^getGPS/$', getGPS),
    url('^sendGPS/$', sendGPS),
]
