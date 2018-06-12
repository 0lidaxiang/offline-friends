#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import sys
# import json
# from django.http import JsonResponse
from user.models import User

from django.shortcuts import render
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup

def sendGPS(request):
    context	= {}

    try:
        id = request.POST['id']
        nickname = request.POST['nickname']
        longitude = float(request.POST['longitude'])
        latitude = float(request.POST['latitude'])

        print("gps index.py", longitude, latitude)
        # userId = userName + "_" + str(int(time.time())) + "_" + str(random.randint(1000))
        # print(userName,password,email)
        status, message = User.modifyLL(id, longitude, latitude)
        # context["status"] = True
        # context["longitude"] = longitude
        # context["latitude"] = latitude

        res_dict = {'status': status, 'message': message}

        return JsonResponse(res_dict)
        # return context
    except Exception as e:
        res_dict = {'status': False, 'message': latitude}
        print(str(e))

    return JsonResponse(res_dict)
