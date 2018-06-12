#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

from home.view.index import  *
# from home.view.computer import  *

urlpatterns = [
    url('^index/$', index),
    url('^index1/$', index1),
    url('^index2/$', index2),
    url('^indexA/$', indexA),
    url('^indexB/$', indexB),
    url('^aboutUs/$', aboutUs),
    url('^computeGPS/$', computeGPS),
    url('^getStepFrenquency/$', getStepFrenquency),
]
