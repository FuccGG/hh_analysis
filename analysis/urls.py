from django.contrib import admin
from django.conf.urls import include, url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
