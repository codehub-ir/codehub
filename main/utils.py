'''
This file contains methods that are being
used as a data generator in the models, views, and etc.
'''


def generateUID(model, nb=5) -> str:
    from secrets import token_hex

    uid = token_hex(nbytes=nb)
    while model.objects.filter(id=uid).exists():
        uid = token_hex(nbytes=nb)

    return uid
