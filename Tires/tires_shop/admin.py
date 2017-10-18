from django.contrib import admin

# Register your models here.
from .models import Tires


@admin.register(Tires)
class TiresAdmin(admin.ModelAdmin):
    pass
