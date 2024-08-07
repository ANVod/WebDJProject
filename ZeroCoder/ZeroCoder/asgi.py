"""
# Конфигурация ASGI для проекта ZeroCoder.
#
# Она предоставляет возможность вызова ASGI в качестве переменной уровня модуля с именем `application`.
#
# Дополнительную информацию об этом файле смотрите в разделе
# https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
# """
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ZeroCoder.settings')

application = get_asgi_application()
