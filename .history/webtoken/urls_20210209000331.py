from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('check_assign/', views.checkAndAssign, name='check_assign'),
]