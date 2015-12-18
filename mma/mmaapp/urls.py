from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.Homepage),
    url(r'^Event/(?P<event_id>[0-9]+$,)', views.EventPage)
    ]