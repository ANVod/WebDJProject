from django.contrib import admin
from django.contrib.auth.models import User

from .models import NewsPost
admin.site.register(NewsPost)
# Register your models here.
