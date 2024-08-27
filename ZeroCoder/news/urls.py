from django.contrib import admin  # Импортируем admin
from django.urls import path  # Импортируем path
from . import views  # Импортируем views

urlpatterns = [
    path('admin/', admin.site.urls),  # Путь для админки
    path('', views.news_list, name='news_home'),  # Исправлено на views.news_list
]
