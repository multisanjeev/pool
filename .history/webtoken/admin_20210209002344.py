from django.contrib import admin
from .models import PoolToken
# Register your models here.

def auto_release(modelAdmin, request, queryset):
    queryset.update(status='A')

class PoolTokenDisplay(admin.ModelAdmin):
    list_display = ('token_key', 'status', 'timeStatus')
    actions = [auto_release]

admin.site.register(PoolToken, PoolTokenDisplay);
