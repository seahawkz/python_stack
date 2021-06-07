import re
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Game, User, Comment

def index(request):
    return render(request, 'login.html')

def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        messages.success(request, "You have successfully registered!")
        return redirect('/dashboard')

def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    return redirect('/dashboard')

def logout(request):
    request.session.clear()
    messages.success(request, "You have successfully logged out!")
    return redirect('/')
    

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user
        
    }
    return render(request, 'dashboard.html', context)

def events(request):
    return render(request, 'events.html', {"games": Game.objects.all()})

def host(request):
    return render(request, 'create.html')

def players(request):
    return render(request, 'users.html', {"users": User.objects.all()})

def dashboard(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
        'games': Game.objects.all()    
    }   
    return render(request, 'dashboard.html', context)

def event(request, game_id):
    game = Game.objects.get(id=game_id)
    context = {
        'game': game,
        'games': Game.objects.all(),   
    }
    return render(request, 'event.html', context)

def create(request):
    if request.method == "POST":
        Game.objects.create(
            game_type = request.POST['game_type'],
            buy_in = request.POST['buy_in'],
            location = request.POST['location'],
            date = request.POST['date'],
            description = request.POST['description'],
            host = User.objects.get(id=request.session['user_id'])
        )
    return redirect('/dashboard')

def comment(request, id):
    poster = User.objects.get(id=request.session['user_id'])
    message = Game.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], poster=poster, game_message=message)
    return redirect('/events')

def join(request, id):
    joined_games = Game.objects.get(id=id)
    user_join = User.objects.get(id=request.session['user_id'])
    joined_games.poker_players.add(user_join)
    return redirect('/dashboard')

def leave(request, id):
    joined_games = Game.objects.get(id=id)
    user_join = User.objects.get(id=request.session['user_id'])
    joined_games.poker_players.remove(user_join)
    return redirect('/dashboard')
