from rest_framework import generics
from snippet.models import Snippet
from .serializers import SnippetSerializer
from rest_framework.response import Response
from rest_framework import status
from snippet.tasks import calendar, sid_generator

class DetailSnippet(generics.RetrieveAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    lookup_field = 'SID'

class AddSnippet(generics.CreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def post(self, request, format=None):
        data = request.data.copy()
        data['SID'] = sid_generator()
        data['pub_date'] = calendar()
        data['link'] = 'http://codehub.pythonanywhere.com/snippet/'+data['SID']
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
