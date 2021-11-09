from django.contrib import admin

from .models import Snippet, Ticket, Tag, Comment


admin.site.register(Snippet)
admin.site.register(Ticket)
admin.site.register(Tag)
admin.site.register(Comment)
