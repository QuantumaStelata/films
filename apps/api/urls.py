from django.urls import path
from .views import FilmsViewSet, FilmDetailViewSet


urlpatterns = [
    path('films/', FilmsViewSet.as_view(), name='api-films'),
    path('films/<str:pk>/', FilmDetailViewSet.as_view(), name='api-film-detail'),
]