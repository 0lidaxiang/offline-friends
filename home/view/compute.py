# -*- coding: UTF-8 -*-

import sys
import time
import random

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators import csrf


from user.models import User

# from django.http import JsonResponse
#
# def computeGPS(request):
#     context	= {}
#     # if "userName" not in request.POST:
#     #     return render(request, 'home/index.html')
#
#     try:
#         id = request.POST['id']
#         nickname = request.POST['nickname']
#         longitude = request.POST['longitude']
#         latitude = request.POST['latitude']
#
#         # userId = userName + "_" + str(int(time.time())) + "_" + str(random.randint(1000))
#         # print(userName,password,email)
#         user = User.getValueByUserId(userId, "all")
#         context["status"] = False
#         context["resCode"] = 11
#         context["mes"] = " fanRegister error "
#
#         # name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
#         return JsonResponse(context)
#         # return context
#     except Exception as e:
#         print(str(e))
#     return JsonResponse(context)
