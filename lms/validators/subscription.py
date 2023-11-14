from rest_framework.serializers import ValidationError

from lms.models import Subscription


class SubscribeValidator:
    def __init__(self, user_field, course_field):
        self.course_field = course_field
        self.user_field = user_field

    def __call__(self, value):
        user = value.get(self.user_field)
        course = value.get(self.course_field)

        if user is None or course is None:
            raise ValidationError('Пользователь и курс должны быть указаны.')

        user_id = user.id
        course_id = course.id

        existing_subscription = Subscription.objects.filter(user=user_id, course=course_id).exists()

        if existing_subscription:
            raise ValidationError('Такая подписка уже существует!')
