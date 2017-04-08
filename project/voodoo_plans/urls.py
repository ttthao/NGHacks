from django.conf.urls import patterns, include, url
from django.contrib import admin
from djongo.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
