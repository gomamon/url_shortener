from django import forms
from .models import *

class URLSearchForm(forms.Form):
    search_url = forms.URLField(label = 'Enter your url', required = True, max_length=250)
