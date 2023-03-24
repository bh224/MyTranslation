from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# celery 기본 django 설정파일
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")

# settings.py 에서 정의한 celery 설정 
app.config_from_object(settings, namespace="CELERY")

app.autodiscover_tasks()

# app.conf.enable_utc = False
# app.conf.update(timezone = 'Asia/Seoul')
# # celery beat settings
# app.conf.beat_schedule = {
# }

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")

