from rest_framework import serializers
from snippet.models import Snippet, Teammate


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
            model = Snippet
            fields = ('SID', 'title', 'detail',
                      'script', 'language', 'pub_date', 'link',)


class TeammateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teammate
        fields = ('name', 'position', 'passion', 'github', 'linkedin',
                  'twitter', 'gmail')
