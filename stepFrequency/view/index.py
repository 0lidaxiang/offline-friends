# -*- coding: UTF-8 -*-

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
        # now_step_num = 140

        id = request.POST['id']
        status, oldStepFrequency = User.getValueByUserId(id, "stepFrequency")
        oldSteps = oldStepFrequency * 10
        nowStepFrequency = (now_step_num - oldSteps) / 10.0
        # print(nowStepFrequency,now_step_num , oldSteps)
        status, message = User.modifyObj(id, "stepFrequency", nowStepFrequency)

        res_dict = {'status': status, 'message': nowStepFrequency}

        return JsonResponse(res_dict)
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



def getStepFrenquencyNow(request):
     devId = request.POST['devId']
     url_str = 'https://mcs.mediatek.com/public/devices/DjQvVy1x/datachannels/' + str(devId) + '?locale=zh-CN'
     req = requests.get(url_str)
     req_text = req.text

     soup = BeautifulSoup(req_text, 'html.parser')
     now_step_num = int(soup.find('div', attrs={'class':'CjCuiMrOmd5M'}).text)
     # print( type(now_step_num), now_step_num  )

     res_dict = {'status': True, 'message': now_step_num }
     return JsonResponse(res_dict)
