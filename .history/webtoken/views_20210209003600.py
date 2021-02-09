from django.shortcuts import render
from django.http import HttpResponse
from .models import PoolToken
from datetime import datetime

# Create your views here.

def autoRefresh(request):
    #PoolToken.objects.filter(status='B', timeStatus__gt = )
    now = datetime.now()
    now_plus_10 = now + now.timedelta(minutes = 10)
    return HttpResponse('now %s and +10 ' % now_plus_10)

def checkAndAssign(request):
    freeToken = PoolToken.objects.filter(status='A')[0:1]
    if freeToken:
        PoolToken.objects.filter(token_key = freeToken[0].token_key).update(status='B', timeStatus = datetime.now().time())
        return HttpResponse('Alive token has been assigned %s' % freeToken[0].token_key)
    return HttpResponse('All token busy, Please try again!')