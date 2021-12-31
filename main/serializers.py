from rest_framework import serializers
from .models import Snippet, Event


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'description', 'body',
                  'lang', 'created_by', 'created_on')


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = ('title', 'body', 'created_on')
