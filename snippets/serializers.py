from rest_framework import serializers

from .models import Snippet


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'description', 'body',
                  'lang', 'created_by', 'created_on')