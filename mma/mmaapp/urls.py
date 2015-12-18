from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.Homepage),
    url(r'^Event/(?P<event_id>[0-9]+)$', views.EventPage),
    url(r'^Fighter/(?P<fighter_id>[0-9]+)$', views.FighterPage),
    url(r'^AddFighter$', views.AddFighter),
    url(r'^AddEvent$', views.AddEvent),
    url(r'^AddFight$', views.AddFight),
    url(r'^RemoveEvent/(?P<event_id>[0-9]+)$', views.RemoveEvent),
    url(r'^RemoveFight/(?P<fight_id>[0-9]+)$', views.RemoveFight),
    ]