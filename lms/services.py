import stripe
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from lms.models import Subscription

stripe.api_key = \
    "sk_test_51OBbACB3yxvsB3AL1CwLvjnFWqPCZBcRFxfM2YwtFfgcRVRNX4FpZBpd5hzwLEChOjVyudkHRKdcV0T7mjHEjgb500O39AXTRY"


def create_payment_intent(amount):
    payment_intent = stripe.PaymentIntent.create(
        amount=int(amount),
        currency="usd",
        automatic_payment_methods={"enabled": True},
    )
    return payment_intent


def get_retrieve_payment(payment_id):
    return stripe.PaymentIntent.retrieve(payment_id)


def subscriber_notice(course_id):
    subscriptions = Subscription.objects.filter(course=course_id)

    for subscription in subscriptions:
        send_mail(
            subject='Курс на который вы подписаны притерпел изменения! Кек-пук',
            message=f'Название: {subscription.course.name}\n'
                    f'Описание: {subscription.course.description}',
            from_email=EMAIL_HOST_USER,
            recipient_list=['gamaizingg@gmail.com'],
            fail_silently=False,
        )
