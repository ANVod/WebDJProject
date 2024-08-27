from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils import timezone

class NewsPost(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор новости')
    author_name = models.CharField('Имя пользователя', max_length=100)  # Новое поле

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

def create_news(request):
    if request.method == "POST":
        title = request.POST.get('title')
        short_description = request.POST.get('short_description')
        text = request.POST.get('text')
        author = request.user  # Получаем текущего пользователя
        author_name = author.username  # Получаем имя пользователя

        # Создание новой записи
        new_post = NewsPost(
            title=title,
            short_description=short_description,
            text=text,
            pub_date=timezone.now(),
            author=author,
            author_name=author_name
        )
        new_post.save()
        return redirect('news_home')
    else:
        return render(request, 'news/create_news.html')

def __str__(self):
    return self.title

class Meta:
    verbose_name = 'Новость'
    verbose_name_plural = 'Новости'