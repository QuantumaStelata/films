from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404

from apps.database.models import Actor, Film
from .services import *

class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/main.html', {**get_recommendations_films(), **get_new_films(), **get_all_genres()})


class FilmView(View):
    def get(self, request, pk, *args, **kwargs):
        film = get_object_or_404(Film, pk = pk, is_delete = False)
        return render(request, 'main/film.html', {'film': film, **get_recommendations_films(), **get_all_genres()})

class GenreView(View):
    def get(self, request, pk, *args, **kwargs):
        genre = get_object_or_404(Genre, pk = pk)
        films = genre.films.filter(is_delete = False)
        return render(request, 'main/genre.html', {'genre': genre, 'films': films, **get_recommendations_films(), **get_all_genres()})

class ActorView(View):
    def get(self, request, pk, *args, **kwargs):
        actor = get_object_or_404(Actor, pk = pk)
        films = actor.films.filter(is_delete = False)
        return render(request, 'main/actor.html', {'actor': actor, 'films': films, **get_recommendations_films(), **get_all_genres()})
