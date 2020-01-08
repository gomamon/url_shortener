from django.urls import path, re_path, include
from django.conf.urls import url
from .views import *
from . import views
app_name = 'shortener'
urlpatterns = [
    url(r'^$',MainView.as_view(),name='main'),
    url(r'^result/(?P<shorten>\w+)/$', views.result_view, name='result' ),
        
    ]
