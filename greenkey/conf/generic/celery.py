import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'greenkey.conf.environments.vagrant')

app = Celery('greenkey_celery')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Set up recurring tasks
app.conf.beat_schedule = {}