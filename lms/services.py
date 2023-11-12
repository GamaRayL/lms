import stripe
import requests

# URL = 'https://api.stripe.com/v1/payment_intents'
stripe.api_key = "sk_test_51OBbACB3yxvsB3AL1CwLvjnFWqPCZBcRFxfM2YwtFfgcRVRNX4FpZBpd5hzwLEChOjVyudkHRKdcV0T7mjHEjgb500O39AXTRY"


def create_payment_intent(amount):
    payment_intent = stripe.PaymentIntent.create(
        amount=int(amount),
        currency="usd",
        automatic_payment_methods={"enabled": True},
    )
    return payment_intent


def get_retrieve_payment(payment_id):
    return stripe.PaymentIntent.retrieve(payment_id)
