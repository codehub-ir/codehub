'''
This file contains methods that are being
used as a data generator in the models, views, and etc.
'''


def generateSID() -> str:
    from secrets import token_hex
    from .models import Snippet

    bytenums = 5

    sid = token_hex(nbytes=bytenums)
    while Snippet.objects.filter(id=sid).exists():
        sid = token_hex(nbytes=bytenums)

    return sid
