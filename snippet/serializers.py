from rest_framework import serializers
from .models import Snippet, Teammate, Suggest


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = (
            'SID', 'title', 'detail',
            'script', 'error', 'language',
            'pub_date', 'link',
        )


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teammate
        fields = (
            'name', 'position', 'passion', 'support_side',
            'github', 'linkedin', 'twitter', 'gmail',
        )


class SuggestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggest
        fields = (
            'title', 'content', 'theme',
        )
