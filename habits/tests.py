from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """ Test case for Habit model """

    def setUp(self):
        """Creating test user and test model"""

        self.user = User.objects.create(
            email="admin@admin",
            password="admin"
        )
        self.client.force_authenticate(user=self.user)
        self.data = {
            "place": "test",
            "time": "7:00:00",
            "action": "test",
            "duration": "0:02:00"
        }
        self.test_obj = Habit.objects.create(**self.data, user=self.user)

    def test_create_habit(self):
        """Testing create"""

        response = self.client.post('/habits/', data=self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.json()['action'], 'test')

    def test_list_habit(self):
        """Testing list"""

        response = self.client.get('/habits/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertTrue(Habit.objects.all().exists())

        self.assertTrue(response.json()['count'] in (1, 2))

    def test_retrieve_habit(self):
        """Testing retrieve"""

        response = self.client.get(f'/habits/{self.test_obj.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                'id': self.test_obj.id,
                "place": "test",
                "time": "07:00:00",
                "action": "test",
                "is_pleasant": False,
                "frequency": "ежедневно",
                "reward": None,
                "duration": "00:02:00",
                "is_public": True,
                "user": self.user.id,
                "related_habit": None
            }
        )

    def test_update_habit(self):
        """Testing update"""
        new_data = {
            "place": "test2",
            "time": "19:00:00",
            "action": "test2",
            "duration": "0:02:00"
        }
        response = self.client.patch(
            f'/habits/{self.test_obj.id}/',
            data=new_data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                'id': self.test_obj.id,
                "place": "test2",
                "time": "19:00:00",
                "action": "test2",
                "is_pleasant": False,
                "frequency": "ежедневно",
                "reward": None,
                "duration": "00:02:00",
                "is_public": True,
                "user": self.user.id,
                "related_habit": None
            }
        )

    def test_delete_habit(self):
        """Testing delete"""

        response = self.client.delete(f'/habits/{self.test_obj.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
