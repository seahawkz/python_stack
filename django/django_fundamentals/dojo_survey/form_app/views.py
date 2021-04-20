from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def process(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'lang': request.POST['language'],
            'loc': request.POST['location'],
            'flu': request.POST.getlist('fluent[]')
        }
        return render(request, 'result.html', context)
    return render(request, 'result.html')