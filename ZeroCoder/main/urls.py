from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)