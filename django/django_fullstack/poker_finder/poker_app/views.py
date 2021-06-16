import re
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Game, User, Comment
from django.contrib.auth.decorators import login_required


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
    if 'user_id' not in request.session:
        messages.error(request, "You must be logged in to view this page!")
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
        'games': Game.objects.all()    
        } 
    return render(request, 'events.html', context)

def host(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request, 'create.html')

def players(request):
    if 'user_id' not in request.session:
        messages.error(request, "You must be logged in to view this page!")
        return redirect('/')
    return render(request, 'users.html', {"users": User.objects.all()})

def dashboard(request):
    if 'user_id' not in request.session:
        messages.error(request, "You must be logged in to view this page!")
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
        'games': Game.objects.all()    
    }   
    return render(request, 'dashboard.html', context)

def event(request, game_id):
    if 'user_id' not in request.session:
        messages.error(request, "You must be logged in to view this page!")
        return redirect('/')
    game = Game.objects.get(id=game_id)
    context = {
        'game': game,
        'games': Game.objects.all(),
        'comments': Comment.objects.all(),
        'users': User.objects.all(),  
    }
    return render(request, 'event.html', context)


def create(request):
    if 'user_id' not in request.session:
        messages.error(request, "You must be logged in to view this page!")
        return redirect('/')
    errors = Game.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/host')
    else:
        if request.method == "POST":
            game = Game.objects.create(
                game_type = request.POST['game_type'],
                buy_in = request.POST['buy_in'],
                location = request.POST['location'],
                date = request.POST['date'],
                description = request.POST['description'],
                host = User.objects.get(id=request.session['user_id'])
                )
            print (game.date)
    return redirect('/dashboard')

def comment(request, id):
    poster = User.objects.get(id=request.session['user_id'])
    message = Game.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], poster=poster, game_message=message)
    return redirect(f'/event/{id}')

def delete_comment(request, id):
    delete_comment = Comment.objects.get(id=id)
    delete_comment.delete()
    return redirect('/dashboard')

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

def profile(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,    
    } 
    return render(request, 'profile.html', context)

def edit(request, id):
    edit_user = User.objects.get(id=id)
    edit_user.first_name = request.POST['first_name']
    edit_user.last_name = request.POST['last_name']
    edit_user.email = request.POST['email']
    edit_user.birthdate = request.POST['birthdate']
    edit_user.save()
    return redirect('/profile')

def delete(request, id):
    delete_game = Game.objects.get(id=id)
    delete_game.delete()
    return redirect('/dashboard')

def edit_game(request, id):
    errors = Game.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect(f'/event/{id}')
    else:
        edit_game = Game.objects.get(id=id)
        edit_game.game_type = request.POST['game_type']
        edit_game.buy_in = request.POST['buy_in']
        edit_game.location = request.POST['location']
        edit_game.date = request.POST['date']
        edit_game.description = request.POST['description']
        edit_game.save()
    return redirect(f'/event/{id}')
