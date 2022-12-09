from django.contrib import admin
from .models import Player, Prize

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ("name",)
    search_fields = ['name']


@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_prize',)
    list_filter = ("total_prize",)
    search_fields = ['total_prize']
