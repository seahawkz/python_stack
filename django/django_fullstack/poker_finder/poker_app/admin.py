from django.contrib import admin
from .models import Comment, User, Game

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("game_type", "buy_in", "location", "date")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment", "poster")