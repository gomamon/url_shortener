from django.utils import timezone
from django.db import models

class Url(models.Model):
    original = models.URLField(max_length=250, blank=False, null=True, unique=True)
    shorten = models.CharField(max_length=8, blank=False, null=True, unique=True)
