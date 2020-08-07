import os

from django.conf import settings
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'acme.settings')

app = Celery('acme', broker=settings.BROKER_URL,
             backend=settings.CELERY_RESULT_BACKEND)

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
