from django.contrib import admin
from .models import Price, Kino


@admin.register(Kino)
class KinoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name information', {'fields': ['kino_name']}),
        ('Description information', {'fields': ['description']}),
        ('Genre information', {'fields': ['genre']}),
        ('Country information', {'fields': ['country']}),
        ('Director information', {'fields': ['director']}),
    ]


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ("name", "money",)
