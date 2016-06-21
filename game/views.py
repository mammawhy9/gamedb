from django.shortcuts import render
from django.views.generic import ListView
from game.models import Game
class IndexView(ListView):
    template_name = "game/index.html"
    model = Game
    def __init__(self):
        self.content_data = {}
