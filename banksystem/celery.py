from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banksystem.settings')

app = Celery('banksystem')

app.config_from_object('django.conf:settings', namespace='CELERY')

#Cargar los módulos de tareas de todas las configuraciones de la aplicación Django registradas.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'calculate_interest': {
        'task': 'calculate_interest',
        'schedule': crontab(0, 0, day_of_month='1'),
    }
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))