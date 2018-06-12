#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from home.view.index import  *

urlpatterns = [
    url('^index/$', index),
    url('^aboutUs/$', aboutUs)
]
