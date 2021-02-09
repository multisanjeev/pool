from django.shortcuts import render
from django.http import HttpResponse
from .models import PoolToken
import datetime
import time

# Create your views here.

def autoRefresh(request):
    busyToken = PoolToken.objects.filter(status='B')
    for token in busyToken:
        tokenDateTime = token.timeStatus + datetime.timedelta(minutes=5)
        tokenUnixtime = time.mktime(tokenDateTime.timetuple())
        nowDate = datetime.datetime.now()
        nowUnixtime = time.mktime(nowDate.timetuple())
        if tokenUnixtime < nowUnixtime :
            PoolToken.objects.filter(token_key = token.token_key).update(status='A', timeStatus = datetime.datetime.now())
            return HttpResponse('token has been released')
    return HttpResponse("All token upto date")

def checkAndAssign(request):
    freeToken = PoolToken.objects.filter(status='A')[0:1]
    if freeToken:
        PoolToken.objects.filter(token_key = freeToken[0].token_key).update(status='B', timeStatus = datetime.datetime.now())
        return HttpResponse('Alive token has been assigned %s' % freeToken[0].token_key)
    return HttpResponse('All token busy, Please try again!')