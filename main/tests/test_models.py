from django.db.models import fields
from django.test import TestCase

from main.models import Snippet, Tag, Ticket
from main.constants import LANGUAGES
from main.utils import generateSID
from account.models import User


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


class TagTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.sample = {
            'name': 'AngularLA',
            'description': 'a framework built in LA',
        }

    def setUp(self):
        self.tag = Tag.objects.create(**self.sample)

    def test_if_obj_returns_same_fields(self):
        fields = {
            'name': self.tag.name,
            'description': self.tag.description,
        }

        self.assertEqual(fields, self.sample)


class TicketTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.ticket_sample = {
            'title': 'Ticket Title',
            'description': 'Ticket Description',
        }

        cls.user_sample = {
            'username': 'johndoe',
            'display_name': 'John Doe',
            'email': 'john@doe.com',
            'password': 'testPass123',
        }

        cls.tag_sample = {
            'name': 'Tag Name',
            'description': 'Tag Description',
        }

    def setUp(self):
        _user = User.objects.create(**self.user_sample)

        '''
        Since the Ticket.tags is a ManyToMany field,
        It needs to get saved immediately right after
        It created.
        '''
        _tag = Tag(**self.tag_sample)
        _tag.save()

        self.ticket = Ticket.objects.create(**self.ticket_sample)
        self.ticket.save()

        '''
        Then we add those pre-built Tag objects to
        the Ticket object tags field. -> Ticket.tags
        '''
        self.ticket.tags.set([_tag])
        self.ticket.created_by = _user

    def test_obj_returns_same_fields(self):
        fields = {
            'title': self.ticket.title,
            'description': self.ticket.description,
        }

        self.assertEqual(fields, self.ticket_sample)

    def test_check_ticket_creator(self):
        self.assertEqual(self.ticket.created_by.username,
                         self.user_sample['username'])
