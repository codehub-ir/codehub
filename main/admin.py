from django.contrib import admin

from snippets.models import Snippet
from tickets.models import Ticket, Tag, Comment
from .models import Event


admin.site.register(Snippet)
admin.site.register(Ticket)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Event)
