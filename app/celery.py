from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

app = Celery("app")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "send-messages-every-5-seconds": {
        "task": "core.tasks.send_messages",
        "schedule": 5.0,
    }
}

app.conf.timezone = "UTC"
app.conf.task_always_eager = True
app.conf.task_eager_propagates = True