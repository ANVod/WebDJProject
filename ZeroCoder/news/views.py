from django.shortcuts import render


def home(request):
    return render(request, 'main/new.html')



# Create your views here.
