from django.db import models
from django_hashids import HashidsField


class Snippet(models.Model):
    # all snippets and code pieces
    
    LANGUAGES = (
        ('', ''),
        ('', ''),
    )
    id = HashidsField(real_field_name='Snippet ID', min_length=10, alphabet=''.join([chr(_) for _ in range(65, 123)]))
    
    '''
    title = models.CharField(max)
    description = models.TextField
    body = models.TextField
    language = 
    created_on = 
    views = 
    '''