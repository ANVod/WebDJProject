from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'main/index.html', {'caption': "CatDjango"})

def new(request):
    return render(request, 'main/new.html')

def home(request):
       return render(request, 'main/home.html')