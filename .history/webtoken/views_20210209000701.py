from django.shortcuts import render
from django.http import HttpResponse
from .models import PoolToken
from datetime import datetime

# Create your views here.

def hello(request):
    PoolToken.objects.filter(token_key = '17ccf828baf20fcfe1c3514d250890f8').update(status='B', 
    timeStatus = datetime.now().time())
    return HttpResponse('First API call')

def checkAndAssign(request):
    freeToken = PoolToken.objects.filter(status='A')
    return HttpResponse(freeToken)