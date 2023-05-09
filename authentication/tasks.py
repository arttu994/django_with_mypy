from celery import shared_task

from authentication.services import send_mail


@shared_task
def send_email(email, uuid):
    send_mail(email, uuid)
