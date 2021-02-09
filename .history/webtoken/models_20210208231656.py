from django.db import models
import secrets
import datetime

# Create your models here.

class PoolToken(models.Model):
    status_token = [('A', 'Alive'), ('B', 'Busy')]
    token_key = models.CharField(default=secrets.token_hex(16))
    status = models.CharField()
