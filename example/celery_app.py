from __future__ import absolute_import

import os

from celery import Celery

from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'example.settings')
app = Celery('example', broker=settings.BROKER_URL)

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
