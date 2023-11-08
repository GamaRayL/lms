from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from constants import EXPECTED_DATA
from lms.models import Lesson
from users.models import User


class LessonTestCase(APITestCase):
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

    def test_create_lesson(self):
        """ Тестирование создания урока """
        data = {
            "name": "New lesson",
            "description": "New lesson description",
            "video_url": "https://www.youtube.com/watch?v=nLRL_NcnK-4"
        }

        response = self.client.post('/lessons/create/', data=data)

        self.assertEqual(response.json(), EXPECTED_DATA)

        self.assertTrue(Lesson.objects.all().exists())

    def test_list_lesson(self):
        """ Тестирование получения списка уроков """

        Lesson.objects.create(
            name="New lesson",
            description="New lesson description",
            video_url="https://www.youtube.com/watch?v=nLRL_NcnK-4"
        )

        response = self.client.get('/lessons/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    EXPECTED_DATA
                ]
            }
        )
