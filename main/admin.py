from django.contrib import admin

from .models import Comment, Snippet, Tag, Ticket, Event

admin.site.register(Snippet)
admin.site.register(Ticket)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Event)
