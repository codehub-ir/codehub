from rest_framework import serializers
from snippet.models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
            model = Snippet
            fields = ('SID', 'title', 'detail', 'script', 'language', 'pub_date', 'link',)
