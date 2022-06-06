from django.contrib import admin
from . import models
from .models import Price

# Register your models here.

class KinoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name information', {'fields': ['kino_name']}),
        ('Description information', {'fields': ['description']}),
        ('Genre information', {'fields': ['genre']}),
        ('Country information', {'fields': ['country']}),
        ('Director information', {'fields': ['director']}),
    ]

admin.site.register(models.Kino, KinoAdmin)


class PriceAdmin(admin.ModelAdmin):
    list_display = ("name", "money",)

admin.site.register(Price, PriceAdmin)