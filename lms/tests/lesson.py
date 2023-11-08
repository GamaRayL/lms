import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from constants import EXPECTED_DATA, UPDATED_EXPECTED_DATA
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
        self.lesson = Lesson.objects.create(
            name="New lesson",
            description="New lesson description",
            video_url="https://www.youtube.com/watch?v=nLRL_NcnK-4"
        )

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

    def test_update_lesson(self):
        """ Тестирование обновления урока """

        data = {
            "name": "Updated lesson",
            "description": "Updated lesson description",
            "video_url": "https://youtube.com/watch?v=nLRL_NcnK-5"
        }

        response = self.client.patch(f'/lessons/update/{self.lesson.id}/', data=json.dumps(data), content_type='application/json')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            UPDATED_EXPECTED_DATA
        )

    def test_update_lesson(self):
        """ Тестирование обновления урока """

        data = {
            "name": "Updated lesson",
            "description": "Updated lesson description",
            "video_url": "https://youtube.com/watch?v=nLRL_NcnK-5"
        }

        response = self.client.patch(f'/lessons/update/{self.lesson.id}/', data=json.dumps(data),
                                     content_type='application/json')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            UPDATED_EXPECTED_DATA
        )
