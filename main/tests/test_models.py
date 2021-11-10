from django.test import TestCase

from main.models import Snippet, Tag
from main.constants import LANGUAGES
from main.utils import generateSID


class SnippetTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.sample = {
            'title': 'simple title',
            'description': 'some description',
            'body': 'code snippet',
            'lang': LANGUAGES[0][1],  # ApacheConf
        }

    def setUp(self):
        Snippet.objects.create(**self.sample)

    def test_if_obj_returns_same_fields(self):
        snippet = Snippet.objects.get(**self.sample)
        fields = {
            'title': snippet.title,
            'description': snippet.description,
            'body': snippet.body,
            'lang': snippet.lang,
        }

        self.assertEqual(fields, self.sample)


class TagTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.sample = {
            'name': 'AngularLA',
            'description': 'a framework built in LA',
        }

    def setUp(self):
        Tag.objects.create(**self.sample)

    def test_if_obj_returns_same_fields(self):
        tag = Tag.objects.get(**self.sample)
        fields = {
            'name': tag.name,
            'description': tag.description,
        }

        self.assertEqual(fields, self.sample)


def TicketTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass
