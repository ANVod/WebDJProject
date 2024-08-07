from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)
]

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")