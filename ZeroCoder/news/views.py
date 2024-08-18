from django.shortcuts import render


def home(request):
    return render(request, 'main/new.html')


from django.shortcuts import render

# Create your views here.
def news(request):
    return render(request, 'news/news.html')