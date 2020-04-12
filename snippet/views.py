# VISUAL IMPORTS
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SnippetForm
# TASK IMPORTS
from .tasks import sid_generator, calendar
# API IMPORTS
from .serializers import SnippetSerializer, TeamSerializer, SuggestSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsAdminOrDenied

from codehub import settings
from .models import Snippet, Suggest, Teammate

# VISUAL -- SIDE


def index(request):
    suggestions = Suggest.objects.all()
    return render(request, 'snippet/index.html', {
        'suggestions': suggestions[::-1]})


def docpage(request):
    return render(request, 'snippet/document.html', {})


def new(request):
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.SID = sid_generator()
            post.title = request.POST.get('title')
            post.detail = request.POST.get('detail')
            post.script = request.POST.get('script')
            post.language = request.POST.get('language')
            post.pub_date = calendar()
            post.link = settings.WEBSITE_ADDR + 'snippet/' + post.SID
            post.save()
            return redirect('show', id=post.SID)
    else:
        form = SnippetForm()
    return render(request, 'snippet/new.html', {'form': form})


def show(request, id):
    query = get_object_or_404(Snippet, SID=id)
    return render(request, 'snippet/snippet.html', {'snippet': query})


def team(request):
    teammates = Teammate.objects.all()
    return render(request, 'snippet/team.html', {'teammates': teammates})


# API -- SIDE


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


class AdminSuggestAdd(generics.ListCreateAPIView):
    permission_classes = (IsAdminOrDenied,)
    queryset = Suggest.objects.all()
    serializer_class = SuggestSerializer


class AdminTeamAdd(generics.ListCreateAPIView):
    permission_classes = (IsAdminOrDenied,)
    queryset = Teammate.objects.all()
    serializer_class = TeamSerializer
