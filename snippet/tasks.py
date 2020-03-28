from . import models
from random import choice
import string
from codehub import settings
from jdatetime import datetime


def sid_generator():
    letters = string.ascii_letters
    id = ''.join(choice(letters) for i in range(10))
    if sid_detector(id):
        sid_generator()
    else:
        return id


def sid_detector(val):
    try:
        query = models.Snippet.objects.get(SID=val)
        return True
    except:
        return False


def calendar():
    date = datetime.now()
    new_day = ''.join([str(settings.PERSIAN_NUM[int(i)]) for i in str(date.day)])
    new_mon = settings.JALALI_CAL[date.month]
    new_year = ''.join([str(settings.PERSIAN_NUM[int(i)]) for i in str(date.year)])
    return '%s %s %s' % (new_day, new_mon, new_year)
