'''
This file contains methods that are being
used as a data generator in the models, views, and etc.
'''


def generateSID(nb=5) -> str:
    from secrets import token_hex
    from .models import Snippet

    sid = token_hex(nbytes=nb)
    while Snippet.objects.filter(id=sid).exists():
        sid = token_hex(nbytes=nb)

    return sid
