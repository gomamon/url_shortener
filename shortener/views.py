from django.shortcuts import render
from .forms import *
from .models import *
from django.urls import reverse
from django.views.generic import View
from django.views.generic.edit import FormView
from django.shortcuts import (get_object_or_404, redirect, render,
                                      render_to_response)
import string
import random

def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class MainView(FormView): 
    template_name = 'shortener/main.html'
    form_class = URLSearchForm
    
    def form_valid(self, form):
        shorten = ''
        search_url = '%s' %self.request.POST['search_url']
        q_url = Url.objects.filter(original = search_url).count()
        
        print(q_url)

        if not q_url:
            URL = Url.objects.create(original = search_url)
            URL.shorten = id_generator() 
            shorten = URL.shorten
            URL.save()
        else:
            URL = get_object_or_404(Url, original = search_url)
            shorten = URL.shorten
    
        return redirect('/result/'+shorten)

def result_view(request, shorten):
    context = {
        'shorten' : shorten,
        'original' : Url.objects.filter(shorten = shorten).first().original
    }
    return render(request, 'shortener/result.html', context)
