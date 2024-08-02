from django.shortcuts import render


def welcome(request):
    return render(request, 'Welcome.html')

def login(request):
    return render(request, 'login.html')

def sign_up(request):
    return render(request, 'sign_up.html')

def home(request):
    return render(request, 'home.html')

def makeup(request):
    return render(request, 'makeup.html')

def skincare(request):
    return render(request, 'skincare.html')
# Create your views here.
