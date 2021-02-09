from django.urls import path
from . import views

urlpatterns = [
    path('', views.autoRefresh, name='autoRefresh'),
    path('check_assign/', views.checkAndAssign, name='check_assign'),
]