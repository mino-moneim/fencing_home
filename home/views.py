from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html', context={'home':home})


def login(request):
    return render (request, 'login.html', context={'login':login})