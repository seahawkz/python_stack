from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('success', views.success),
    path('create', views.create),
    path('events', views.events),
    path('players', views.players),
    path('host', views.host),
    path('dashboard', views.dashboard),
    path('event/<int:game_id>', views.event),
    path('comment/<int:id>', views.comment),
    path('join/<int:id>', views.join),
    path('leave/<int:id>', views.leave),
    path('profile', views.profile),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete),
    path('delete_comment/<int:id>', views.delete_comment),
    path('event/edit/<int:id>', views.edit_game)

]