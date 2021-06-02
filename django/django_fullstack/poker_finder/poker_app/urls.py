from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('dashboard', views.success),
    path('create', views.host),
    path('events', views.events),
    path('players', views.players),
]