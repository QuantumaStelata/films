from django.urls import path
from .views import FilmsViewSet, FilmDetailViewSet, \
                   GenresViewSet, GenreDetailViewSet, \
                   ActorsViewSet, ActorDetailViewSet


urlpatterns = [
    path('films/', FilmsViewSet.as_view(), name='api-films'),
    path('films/<str:pk>/', FilmDetailViewSet.as_view(), name='api-film-detail'),

    path('genres/', GenresViewSet.as_view(), name='api-genres'),
    path('genres/<str:pk>/', GenreDetailViewSet.as_view(), name='api-genre-detail'),
    
    path('actors/', ActorsViewSet.as_view(), name='api-actors'),
    path('actors/<str:pk>/', ActorDetailViewSet.as_view(), name='api-actors-detail'),
]