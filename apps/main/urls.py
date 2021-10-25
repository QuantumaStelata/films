from django.urls import path

from .views import MainView, FilmView

urlpatterns = [
    path('', MainView.as_view(), name = 'main'),
    path('film/<str:pk>', FilmView.as_view(), name = 'film'),
]