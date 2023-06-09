import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_with_mypy.settings.settings")

app = Celery("django_with_mypy")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
