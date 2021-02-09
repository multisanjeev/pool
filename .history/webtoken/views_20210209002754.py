from django.shortcuts import render
from django.http import HttpResponse
from .models import PoolToken
from datetime import datetime

# Create your views here.

def autoRefresh(request):
    PoolToken.objects.filter(status='B')
    return HttpResponse('First API call')

def checkAndAssign(request):
    freeToken = PoolToken.objects.filter(status='A')[0:1]
    if freeToken:
        PoolToken.objects.filter(token_key = freeToken[0].token_key).update(status='B', timeStatus = datetime.now().time())
        return HttpResponse('Alive token has been assigned %s' % freeToken[0].token_key)
    return HttpResponse('All token busy, Please try again!')