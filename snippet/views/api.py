from snippet.serializers import SnippetSerializer, TeamSerializer, SuggestSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from snippet.permissions import IsAdminOrDenied

from codehub import settings
from snippet.models import Snippet, Suggest, Teammate

from snippet.tasks import sid_generator, calendar


class SnippetView(generics.RetrieveAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    lookup_field = 'SID'


class SnippetAdd(generics.CreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def post(self, request, format=None):
        data = request.data.copy()
        data['SID'] = sid_generator()
        data['pub_date'] = calendar()
        data['link'] = '%ssnippet/%s' % (settings.WEBSITE_ADDR, data['SID'])
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamView(generics.ListAPIView):
    queryset = Teammate.objects.all()
    serializer_class = TeamSerializer


class AdminSnippetView(generics.ListAPIView):
    permission_classes = (IsAdminOrDenied,)
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class AdminSnippetMod(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminOrDenied,)
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    lookup_field = 'SID'


class AdminSuggestAdd(generics.ListCreateAPIView):
    permission_classes = (IsAdminOrDenied,)
    queryset = Suggest.objects.all()
    serializer_class = SuggestSerializer


class AdminSuggestMod(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminOrDenied,)
    queryset = Suggest.objects.all()
    serializer_class = SuggestSerializer


class AdminTeamAdd(generics.ListCreateAPIView):
    permission_classes = (IsAdminOrDenied,)
    queryset = Teammate.objects.all()
    serializer_class = TeamSerializer


class AdminTeamMod(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminOrDenied,)
    queryset = Teammate.objects.all()
    serializer_class = TeamSerializer
