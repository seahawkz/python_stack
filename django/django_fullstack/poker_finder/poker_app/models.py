from typing import NoReturn
from django.db import models
from datetime import datetime
import re

from django.db.models.fields.related import ManyToManyField
import bcrypt


# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class LoginManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['first_name']) < 2:
            errors['first_name'] = 'First Name must be at least 2 characters long!'
        
        if len(form['last_name']) < 2:
            errors['last_name'] = 'Last Name must be at least 2 characters'

        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Invalid Email Address'
        
        email_check = self.filter(email=form['email'])
        if email_check:
            errors['email'] = "Email already in use"

        if len(form['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        
        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'

        birthdate = form['birthdate']
        date_object = datetime.strptime(birthdate, "%Y-%m-%d")
        present = datetime.now()
        if date_object.date() > present.date():
            errors['birthdate'] = "You can't be born in the future!"

        return errors

    def authenticate(self, email, password):
        users = self.filter(email=email)
        if not users:
            return False

        user = users[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())

    def register(self, form):
        pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name = form['first_name'],
            last_name = form['last_name'],
            email = form['email'],
            birthdate= form['birthdate'],
            password = pw,
        )

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    birthdate = models.DateField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def viewbirthdate(self):
        return '{}'.format(self.birthdate)
    objects = LoginManager()

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

class EventManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['game_type']) < 2:
            errors['game_type'] = 'Game type must be at least 2 characters long!'
        
        if len(form['buy_in']) < 1:
            errors['last_name'] = 'You must provide the buy in cost!'

        if len(form['location']) < 2:
            errors['location'] = 'Location must be at least 2 characters long!'

        date = form['date']
        date_object = datetime.strptime(date, "%Y-%m-%d")
        present = datetime.now()
        if date_object.date() < present.date():
            errors['date'] = "Events can't be scheduled in the past!"
        if date_object.date() == None:
            errors['date'] = "You must enter a date"
        return errors

class Game(models.Model):
    game_type = models.CharField(max_length=255)
    buy_in = models.CharField(max_length=45)
    location = models.CharField(max_length=255)
    date = models.DateField()
    host = models.ForeignKey(User, related_name='host', on_delete=models.CASCADE)
    poker_players = models.ManyToManyField(User, related_name='poker_players')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def dateview(self):
        return '{}'.format(self.date)
    objects = EventManager()

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    game_message = models.ForeignKey(Game, related_name="game_comments", on_delete=models.CASCADE)


