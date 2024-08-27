from django.shortcuts import render
from .models import NewsPost


# #def news(request):
#     news = News_post.objects.all()
#     return render(request, 'news/news.html', {'news': news})
def news_list(request):
    news = NewsPost.objects.all()
    return render(request, 'news/news.html', {'news': news})
