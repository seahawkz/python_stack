from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('dashboard', views.success),
    path('create', views.create),
    path('events', views.events),
    # path('search', views.search),
]