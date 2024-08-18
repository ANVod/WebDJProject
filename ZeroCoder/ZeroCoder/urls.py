# """
# Настройка URL-адресов для проекта ZeroCoder.
#
# Список urlpatterns перенаправляет URL-адреса в представления. Дополнительную информацию смотрите в разделе:
# https://docs.djangoproject.com/en/5.1/topics/http/urls/
# Примеры:
# Представления функций
# 1. Добавьте импорт: из my_app импортируйте представления
# 2. Добавьте URL-адрес в urlpatterns: path(", views.home, name='home")
# Представления на основе классов
# 1. Добавьте импорт: из other_app.views импортируйте Home
# 2. Добавьте URL-адрес в urlpatterns: path(", Home.as_view(), name="home")
# Включая другой URLconf.
# 1. Импортируем функцию include(): из django.urls импортируем include, path
# 2. Добавляем URL в urlpatterns: path('блог/', include('блог.urls'))
# """
from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('', include('main.urls')),
    path('news/', include('news.urls'))
]