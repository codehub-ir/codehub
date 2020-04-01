from django.shortcuts import render, redirect, get_object_or_404
from .forms import SnippetForm
from .models import Snippet, Suggest, Teammate
from .tasks import sid_generator, calendar
from codehub import settings


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
