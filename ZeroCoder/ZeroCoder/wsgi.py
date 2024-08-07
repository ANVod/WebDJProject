"""
# Конфигурация WSGI для проекта ZeroCoder.
#
# Она предоставляет возможность вызова WSGI в качестве переменной уровня модуля с именем `application`.
#
# Дополнительную информацию об этом файле смотрите в разделе
# https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
# """

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ZeroCoder.settings')

application = get_wsgi_application()
