from django.test import TestCase
from accounts.models import User  # Codehub custom user model

from django.contrib.auth import login


class UserTestCase(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.sample = {
            'username': 'JohnDoe',
            'email': 'john@doe.com',
            'display_name': 'John',
            'password': 'test123!',
        }

    def setUp(self) -> None:
        self.user = User.objects.create(**self.sample)

    def test_if_obj_returns_same_fields(self):
        fields = {
            'username': self.user.username,
            'email': self.user.email,
            'display_name': self.user.display_name,
            'password': self.user.password,
        }
        print(self.user.password)
        #self.assertEqual(fields, self.sample)

    # TODO: testing user authentication
    #def test_if_user_can_login(self):
    #    pass
