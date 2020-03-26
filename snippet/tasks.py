from .models import Snippet
from random import choice as rnd
import string
from codehub import settings
from jdatetime import datetime


def generator():
    lnk = ''.join([rnd(string.ascii_letters) for i in range(10)])
    if detector(lnk):
        generator()
    else:
        return lnk


def detector(val):
    try:
        query = Snippet.objects.get(SID=val)
        return True
    except:
        return False

def calendar():
    date = datetime.now()
    new_day = ''.join([settings.PERSIAN_NUM[int(i)] for i in str(date.day)])
    new_mon = settings.JALALI_CAL[date.month]
    new_year = ''.join([settings.PERSIAN_NUM[int(i)] for i in str(date.year)])
    print('%s %s %s'%(new_year, new_mon, new_day))
    return '%s %s %s'%(new_day, new_mon, new_year)
