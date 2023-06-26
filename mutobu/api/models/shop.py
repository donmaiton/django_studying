import datetime

from django.db import models
from django.utils import timezone

class Shop(models.Model):
    name = models.CharField(max_length=255, null=False)
    url = models.URLField(max_length=255, null=False)
    tel = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=255, null=True)
    note = models.TextField(max_length=4000, null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    
