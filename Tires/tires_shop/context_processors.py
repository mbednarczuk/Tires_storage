import datetime

from .models import Tires


def tires_context(request):
    ctx = {
        'date': datetime.datetime.now(),
        'tires': Tires.objects.all(),
    }
    return ctx