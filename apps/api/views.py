from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from apps.database.models import Film, Actor, Genre, Rating
from .serializers import FilmsSerializer, FilmDetailSerializer, \
                         GenresSerializer, GenreDetailSerializer, \
                         ActorsSerializer, ActorDetailSerializer

from django.conf import settings

from .services import is_int

class ApiViewSet(APIView):
    def get(self, request):
        data = {
            "films": f"{settings.HOST}/api/films",
            "actors": f"{settings.HOST}/api/actors",
            "genres": f"{settings.HOST}/api/genres"
        }
        return Response(data)

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

class RatingViewSet(APIView):
    def post(self, request, pk_film):
        film = get_object_or_404(Film, pk = pk_film)
        grade = is_int(request.data.get('grade'))
        ip = request.META['REMOTE_ADDR']
        
        if grade:
            if 1 <= grade and grade <= 10:
                rate, _ = Rating.objects.get_or_create(film = film, ip = ip)
                rate.grade = grade
                rate.save()

                return Response({'status': 'ok'})

            return Response({'status': 'error', 'message': 'grade less than 1 or more than 10'})
        
        return Response({'status': 'error', 'message': 'grade not integer'})
