from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contactus/$', views.contactus, name='contactus'),
    url(r'^subscribe/$', views.subscribe, name='subscribe'),
]