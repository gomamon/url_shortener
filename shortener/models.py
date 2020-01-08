from django.utils import timezone
from django.db import models

class Url(models.Model):
    original = models.URLField(max_length=2500, blank=True, null=False, unique=True)
    shorten = models.CharField(max_length=8, blank=True, null=False, unique=True)
    
class History(models.Model):
    recent_url = models.CharField(max_length=8, default = 'zzzzzzzz')

