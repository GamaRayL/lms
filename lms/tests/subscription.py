from users.models import User
from rest_framework import status
from lms.models import Course, Subscription
from rest_framework.test import APITestCase, APIClient


class SubscriptionTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(
            email='admin@test.com',
            role='admin',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        self.user.set_password('admin')
        self.user.save()
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            name='New course',
            description='New course description'
        )

        self.subscription = Subscription.objects.create(
            user=self.user,
            course=self.course
        )

    def test_get_list_subscription(self):
        """ Тестирование получения списка подписок """
        response = self.client.get('/subscriptions/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{
                "id": 1,
                "is_active": True,
                "user": 1,
                "course": 1
            }]
        )

    def test_create_subscription(self):
        """ Тестирование создания подписки """
        data = {
            "user": 1,
            "course": 1
        }

        response = self.client.post('/subscriptions/', data=data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {
            "id": 2,
            "is_active": False,
            "user": 1,
            "course": 1
        })

    def test_delete_subscription(self):
        """ Тестирование удаления подписки """

        response = self.client.delete(f'/subscriptions/{self.subscription.id}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
