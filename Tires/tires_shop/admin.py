from django.contrib import admin

# Register your models here.
from .models import Tires, BrandsDescribe, Order


@admin.register(Tires)
class TiresAdmin(admin.ModelAdmin):
    pass

@admin.register(BrandsDescribe)
class BrandsDescribeAdmin(admin.ModelAdmin):
    pass
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ( 'quantity', 'order_tire', 'user', )