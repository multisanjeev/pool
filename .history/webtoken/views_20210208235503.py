from django.shortcuts import render
from django.http import HttpResponse
from .models import PoolToken

# Create your views here.

def hello(request):
    PoolToken.object.filter(token_key = '17ccf828baf20fcfe1c3514d250890f8').update(status='A')
    return HttpResponse('Hello')