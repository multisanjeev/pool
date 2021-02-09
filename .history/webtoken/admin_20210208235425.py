from django.contrib import admin
from .models import PoolToken
# Register your models here.

class PoolTokenDisplay(admin.ModelAdmin):
    list_display = ('token_key', 'status', 'timeStatus')

admin.site.register(PoolToken, PoolTokenDisplay);
