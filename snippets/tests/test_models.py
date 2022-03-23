from django.test import TestCase

from snippets.constants import LANGUAGES
from snippets.models import Snippet


class SnippetTestCase(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.sample = {
            'title': 'simple title',
            'description': 'some description',
            'body': 'code snippet',
            'lang': LANGUAGES[0][1],  # Arduino
        }

    def setUp(self) -> None:
        self.snippet = Snippet.objects.create(**self.sample)

    def test_if_obj_returns_same_fields(self):
        fields = {
            'title': self.snippet.title,
            'description': self.snippet.description,
            'body': self.snippet.body,
            'lang': self.snippet.lang,
        }
        self.assertEqual(fields, self.sample)

    def test_sid_length(self):
        # nbyte is set to 5 by default
        # which provides an id with 10 chars
        self.assertEqual(len(self.snippet.id), 10)