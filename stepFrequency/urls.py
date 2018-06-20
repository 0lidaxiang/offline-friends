#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from stepFrequency.view.index import  *

urlpatterns = [
    url('^getStepFrequency/$', getStepFrequency),
    url('^getStepFrenquencyNow/$', getStepFrenquencyNow),
    url('^sendStepFrequency/$', sendStepFrequency),
]
