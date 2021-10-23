from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from apps.database.models import Film, Actor, Genre
from .serializers import FilmsSerializer, FilmDetailSerializer, \
                         GenresSerializer, GenreDetailSerializer, \
                         ActorsSerializer, ActorDetailSerializer


class FilmsViewSet(APIView):
    def get(self, request):
        queryset = Film.objects.filter(is_delete = False)
        serializer = FilmsSerializer(queryset, many = True, read_only = True)
        return Response(serializer.data)

class FilmDetailViewSet(APIView):
    def get(self, request, pk):
        queryset = get_object_or_404(Film, pk = pk, is_delete = False)
        serializer = FilmDetailSerializer(queryset, many = False, read_only = True)
        return Response(serializer.data)

class GenresViewSet(APIView):
    def get(self, request):
        queryset = Genre.objects.all()
        serializer = GenresSerializer(queryset, many = True, read_only = True)
        return Response(serializer.data)

class GenreDetailViewSet(APIView):
    def get(self, request, pk):
        queryset = get_object_or_404(Genre, pk = pk)
        serializer = GenreDetailSerializer(queryset, many = False, read_only = True)
        return Response(serializer.data)

class ActorsViewSet(APIView):
    def get(self, request):
        queryset = Actor.objects.all()
        serializer = ActorsSerializer(queryset, many = True, read_only = True)
        return Response(serializer.data)

class ActorDetailViewSet(APIView):
    def get(self, request, pk):
        queryset = get_object_or_404(Actor, pk = pk)
        serializer = ActorDetailSerializer(queryset, many = False, read_only = True)
        return Response(serializer.data)