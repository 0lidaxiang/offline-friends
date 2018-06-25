# -*- coding: UTF-8 -*-

from user.models import User

from math import radians, cos, sin, asin, sqrt
from django.shortcuts import render
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup

# 更新 database 里面用户的 gps 信息
def sendGPS(request):
    context	= {}

    try:
        id = request.POST['id']
        nickname = request.POST['nickname']
        longitude = float(request.POST['longitude'])
        latitude = float(request.POST['latitude'])

        status, message = User.modifyLL(id, longitude, latitude)
        res_dict = {'status': status, 'message': message}
        return JsonResponse(res_dict)
        # return context
    except Exception as e:
        res_dict = {'status': False, 'message': latitude}
        print(str(e))

    return JsonResponse(res_dict)

# 获得当前用户的存储 gps 位置
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


# 计算两个经纬度之间的距离
# 经度1，纬度1，经度2，纬度2 （十进制度数）
def haversine(lon1, lat1, lon2, lat2):
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
    # 地球平均半径，单位为公里
    r = 6356.752

    return c * r * 1000

# 获得最近的人的列表以及他们的相关 data
def getPeople(request):
    context	= {}
    try:
        id = request.POST['id']

        # 获取除了用户本身以外同一个城市的所有用户 data
        status, userObjs = User.getAllUserGPS(id)
        userObjs = userObjs.exclude(id=id)

        # 获取当前用户的 data
        status, myGPS = User.getValueByUserId(id, "all")

        distance = 0
        neighbors = []
        neighbor = dict()

        # 循环计算当前城市里距离用户最近的其他用户 data ，距离、gps、昵称、性别
        for obj in userObjs:
            distance = haversine(float(myGPS.longitude), float(myGPS.latitude), float(obj.longitude), float(obj.latitude),)
            if distance < 5000:
                neighbor["longitude"] = obj.longitude
                neighbor["latitude"] = obj.latitude
                neighbor["nickname"] = obj.nickname
                neighbor["age"] = obj.age
                neighbor["gender"] = obj.gender
                neighbor["location"] = obj.location
                neighbor["stepFrequency"] = obj.stepFrequency
                neighbor["hobby"] = obj.hobby
                neighbor["distance"] = distance
                neighbors.append(neighbor)

        message = {"myGPS" : {"longitude": myGPS.longitude, "latitude": myGPS.latitude}, "neighbors": neighbors}
        # print("message : ", message)
        res_dict = {'status': status, 'message': message}
        return JsonResponse(res_dict)
    except Exception as e:
        res_dict = {'status': False, 'message': context}
        print(str(e))

    return JsonResponse(res_dict)
