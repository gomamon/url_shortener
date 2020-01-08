from django.shortcuts import render
from .forms import *
from .models import *
from .utils import *

from django.urls import reverse
from django.views.generic import View
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404, redirect, render, render_to_response


class MainView(FormView): 
    template_name = 'shortener/main.html'
    form_class = URLSearchForm
    
    def form_valid(self, form):
        shorten = ''
        search_url = '%s' %self.request.POST['search_url']
        url_count = Url.objects.filter(original = search_url).count()

        if not url_count:
            history_count = History.objects.count()
            if not history_count:
                history = History.objects.create(recent_url = 'ffffffff')
            else:
                history = History.objects.all()[0]

            recent = history.recent_url
            shorten = get_next_alphanum(str(recent))
            print(shorten)
            history.recent_url = shorten
            URL = Url.objects.create(original = search_url, shorten = shorten)
            URL.save()
            history.save()
        else:
            URL = get_object_or_404(Url, original = search_url)
            shorten = URL.shorten
 
        return redirect('/result/'+shorten)


def result_view(request, shorten):
    context = {
        'shorten' : shorten,
        'original' : Url.objects.get(shorten = shorten).original
    }
    return render(request, 'shortener/result.html', context)


def url_mapping_view(request, shorten):
    try:
        URL = Url.objects.get(shorten = shorten)
    except Url.DoesNotExist:
        return render_to_response('/shortner/error.html')
    original = URL.original
    return redirect(original)
