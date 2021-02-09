from django.shortcuts import render
from django.http import HttpResponse
from .models import PoolToken
import datetime
import time

# Create your views here.

def autoRefresh(request):
    busyToken = PoolToken.objects.filter(status='B')
    for token in busyToken:
        d = datetime.date(2015,1,5)
        unixtime = time.mktime(d.timetuple())
        return HttpResponse(unixtime)
    return HttpResponse("Auto refresh token")

def checkAndAssign(request):
    freeToken = PoolToken.objects.filter(status='A')[0:1]
    if freeToken:
        PoolToken.objects.filter(token_key = freeToken[0].token_key).update(status='B', timeStatus = datetime.datetime.now())
        return HttpResponse('Alive token has been assigned %s' % freeToken[0].token_key)
    return HttpResponse('All token busy, Please try again!')