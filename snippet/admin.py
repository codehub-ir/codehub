from django.contrib import admin
from .models import Snippet, Suggest, Teammate


admin.site.register(Snippet)
admin.site.register(Suggest)
admin.site.register(Teammate)
