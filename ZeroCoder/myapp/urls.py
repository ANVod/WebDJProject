from django.urls import path
from .views import data_view, test_view

urlpatterns = [
    path('data/', data_view, name='data'),
    path('test/', test_view, name='test'),
]