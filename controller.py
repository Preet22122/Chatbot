import random

from django.http import HttpResponse
from django.shortcuts import render
import pandas
from mychatserver import *


def opendemo1(request):
    return render(request,'demo1.html')

def openchatbotdemo(request):
    return render(request,'chatbotdemo.html')

def messageReply(request):
    msg=request.GET['msg']
    response = mychatserver.getResponse('', msg)
    l = len(response)
    if l == 0:
        return HttpResponse('sorry we dont understant you')
    else:
        response = list(response)
        n = (int)(random.uniform(0, len(response)))
    return HttpResponse(response[n])

