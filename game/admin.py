from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from game.models import Game


@admin.register(Game)
class Game(SimpleHistoryAdmin):
    list_display = ['title',]
    search_fields = ['title']
