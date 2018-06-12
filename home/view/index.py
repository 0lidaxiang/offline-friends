#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import sys
# import json
# from django.http import JsonResponse
# from book.models import book

from django.shortcuts import render
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup

def index(request):
    context	= {}
    return render(request, 'home/index.html', context)

def indexA(request):
    context	= {}
    return render(request, 'home/indexA.html', context)

def indexB(request):
    context	= {}
    return render(request, 'home/indexB.html', context)

def aboutUs(request):
    context	= {}
    return render(request, 'home/aboutUs.html', context)

# https://mcs.mediatek.com/public/devices/DjQvVy1x/datachannels/5?locale=zh-CN
# https://mcs.mediatek.com/public/devices/DjQvVy1x/datachannels/6?locale=zh-CN

def getStepFrenquency(request):
     id = request.POST['id']
     url_str = 'https://mcs.mediatek.com/public/devices/DjQvVy1x/datachannels/' + str(id) + '?locale=zh-CN'
     req = requests.get(url_str)
     req_text = req.text

     soup = BeautifulSoup(req_text, 'html.parser')
     # print(soup.prettify(), "\n ssssssssss \n")
     now_step_num = int(soup.find('div', attrs={'class':'CjCuiMrOmd5M'}).text)
     print( type(now_step_num), now_step_num  )

     res_dict = {'status': True, 'message': now_step_num }

     # return JsonResponse(res_dict, safe=False)
     return JsonResponse(res_dict)

def computeGPS(request):
    print("ssssssssssssss\n")
    context	= {}

    try:
        id = request.POST['id']
        nickname = request.POST['nickname']
        longitude = request.POST['longitude']
        latitude = request.POST['latitude']

        print(longitude, latitude)
        # userId = userName + "_" + str(int(time.time())) + "_" + str(random.randint(1000))
        # print(userName,password,email)
        # user = User.getValueByUserId(userId, "all")
        # context["status"] = True
        # context["longitude"] = longitude
        # context["latitude"] = latitude

        res_dict = {'status': True, 'message': latitude}

        return JsonResponse(res_dict)
        # return context
    except Exception as e:
        res_dict = {'status': False, 'message': latitude}
        print(str(e))

    return JsonResponse(res_dict)
