from django.conf.urls import *
from raports import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^generate', views.generate, name='generate'),
    url(r'^$', views.sview, name='raports'),
)