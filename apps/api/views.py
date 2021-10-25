from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from apps.database.models import Film, Actor, Genre, Rating, Comment
from .serializers import FilmsSerializer, FilmDetailSerializer, \
                         GenresSerializer, GenreDetailSerializer, \
                         ActorsSerializer, ActorDetailSerializer

from django.conf import settings

from .services import is_int
from django.utils import formats

class ApiViewSet(APIView):
    def get(self, request):
        data = {
            "films": f"{settings.HOST}/api/films",
            "actors": f"{settings.HOST}/api/actors",
            "genres": f"{settings.HOST}/api/genres"
        }

        if not request.user.is_anonymous:
            data['ratings'] = f"{settings.HOST}/api/ratings"
            data['comments'] = f"{settings.HOST}/api/comments"

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
    def post(self, request):
        pk = request.data.get('id')
        film = get_object_or_404(Film, pk = pk)
        grade = is_int(request.data.get('grade'))
        ip = request.META['REMOTE_ADDR']
        
        if grade:
            if 1 <= grade and grade <= 10:
                rate, _ = Rating.objects.get_or_create(film = film, ip = ip)
                rate.grade = grade
                rate.save()

                film = get_object_or_404(Film, pk = pk)

                new_avarage_rating = film.average_rating
                new_ratings_count = film.grades.all().count()

                return Response({'status': 'ok', 'new_avarage_rating': new_avarage_rating, 'new_ratings_count': new_ratings_count})

            return Response({'status': 'error', 'message': 'grade less than 1 or more than 10'})
        
        return Response({'status': 'error', 'message': 'grade not integer'})

class CommentViewSet(APIView):
    def post(self, request):
        pk = request.data.get('id')
        film = get_object_or_404(Film, pk = pk)
        name = request.data.get('name')
        text = request.data.get('text')
        ip = request.META['REMOTE_ADDR']
        
        if name and text:
            if len(name) <= 255 and len(text) <= 255:
                comment = Comment.objects.create(film = film, name = name, text = text, ip = ip)

                # Formating
                get_date = formats.date_format(comment.date_create, format="DATE_FORMAT", use_l10n=True)
                get_time = formats.date_format(comment.date_create, format="TIME_FORMAT", use_l10n=True)

                date_create = f"{get_date} {get_time}"

                return Response({'status': 'ok', 'date_create': date_create})

            return Response({'status': 'error', 'message': 'length name or text is longer than 255 symbols'})
        
        return Response({'status': 'error', 'message': 'not found name or text'})
