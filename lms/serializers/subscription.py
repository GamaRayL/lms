from lms.models import Subscription
from rest_framework import serializers

from lms.validators.subscription import SubscribeValidator


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        validators = [
            SubscribeValidator(user_field='user', course_field='course')
        ]
