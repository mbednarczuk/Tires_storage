import datetime

from .models import Tires, BrandsDescribe, Order


def my_cp(request):
    ctx = {
        'date': datetime.datetime.now(),

    }
    return ctx


def tires_context(request):
    ctx = {
        'tires': Tires.objects.all(),
    }
    return ctx


def describe_context(request):
    ctx = {
        'describe': BrandsDescribe.objects.all(),
    }
    return ctx


def orders_context(request):
    ctx = {
        'orders': Order.objects.all(),
    }
    return ctx
