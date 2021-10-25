from django.urls import path

from .views import MainView, FilmView, GenreView, ActorView

urlpatterns = [
    path('', MainView.as_view(), name = 'main'),
    path('film/<str:pk>', FilmView.as_view(), name = 'film'),
    path('genre/<str:pk>', GenreView.as_view(), name = 'genre'),
    path('actor/<str:pk>', ActorView.as_view(), name = 'actor'),
]