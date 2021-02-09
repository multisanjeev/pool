from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('check_assign/', views.hello, name='check_assign'),
]