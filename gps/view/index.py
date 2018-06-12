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


def getGPS(request):
    context	= {}
    try:
        id = request.POST['id']
        status, res = User.getValueByUserId(id, "all")
        message = {"longitude" : res.longitude, "latitude" : res.latitude}
        res_dict = {'status': status, 'message': message}
        return JsonResponse(res_dict)
    except Exception as e:
        res_dict = {'status': False, 'message': context}
        print(str(e))

    return JsonResponse(res_dict)

from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2): # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # 地球平均半径，单位为公里
    return c * r * 1000

def getPeople(request):
    context	= {}
    try:
        id = request.POST['id']
        status, userObjs = User.getAllUserGPS(id)
        # message = {"longitude" : res, "latitude" : res}


        status, myGPS = User.getValueByUserId(id, "all")

        distance = 0

        for obj in userObjs:
            distance = haversine(float(myGPS.longitude), float(myGPS.latitude), float(obj.longitude), float(obj.latitude),)
            print(distance)
        res_dict = {'status': status, 'message': distance}
        return JsonResponse(res_dict)
    except Exception as e:
        res_dict = {'status': False, 'message': context}
        print(str(e))

    return JsonResponse(res_dict)
