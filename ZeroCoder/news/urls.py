from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.news, name='news_home'),
    path('app_name/', include('app_name.urls'))
]
