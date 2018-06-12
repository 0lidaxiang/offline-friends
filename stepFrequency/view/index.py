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
from user.models import User

def sendStepFrequency(request):
    context	= {}
    try:
        id = request.POST['id']
        devId = request.POST['devId']
        url_str = 'https://mcs.mediatek.com/public/devices/DjQvVy1x/datachannels/' + devId + '?locale=zh-CN'
        req = requests.get(url_str)
        req_text = req.text

        soup = BeautifulSoup(req_text, 'html.parser')
        # print(soup.prettify(), "\n ssssssssss \n")
        now_step_num = int(soup.find('div', attrs={'class':'CjCuiMrOmd5M'}).text)
        # userId = userName + "_" + str(int(time.time())) + "_" + str(random.randint(1000))
        # print(userName,password,email)
        print("sendStepFrenquency: ", type(now_step_num), now_step_num)
        status, message = User.modifyObj(id, "stepFrequency", now_step_num)
        # context["status"] = True
        # context["longitude"] = longitude
        # context["latitude"] = latitude

        res_dict = {'status': status, 'message': message}

        return JsonResponse(res_dict)
        # return context
    except Exception as e:
        res_dict = {'status': False, 'message': context}
        print(str(e))

    return JsonResponse(res_dict)


def getStepFrequency(request):
    context	= {}
    try:
        id = request.POST['id']
        status, message = User.getValueByUserId(id, "stepFrequency")
        res_dict = {'status': status, 'message': message}
        return JsonResponse(res_dict)
    except Exception as e:
        res_dict = {'status': False, 'message': context}
        print(str(e))

    return JsonResponse(res_dict)

# def sendStepFrenquency(request):
#
#      id = request.POST['id']
#      url_str = 'https://mcs.mediatek.com/public/devices/DjQvVy1x/datachannels/' + str(id) + '?locale=zh-CN'
#      req = requests.get(url_str)
#      req_text = req.text
#
#      soup = BeautifulSoup(req_text, 'html.parser')
#      # print(soup.prettify(), "\n ssssssssss \n")
#      now_step_num = int(soup.find('div', attrs={'class':'CjCuiMrOmd5M'}).text)
#      print( type(now_step_num), now_step_num  )
#
#      res_dict = {'status': True, 'message': now_step_num }
#
#      # return JsonResponse(res_dict, safe=False)
#      return JsonResponse(res_dict)
