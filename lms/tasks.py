from celery import shared_task

from lms.services import subscriber_notice


@shared_task
def notification_task(value):
    return subscriber_notice(value)
