from rest_framework import serializers

from apps.database.models import Film, Actor, Genre

from django.conf import settings

class FilmsSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Film
        fields = ('url', 'title', 'year', 'average_rating')

    
    def get_url(self, obj):
        return f"{settings.HOST}/api/films/{obj.id}"

    def get_average_rating(self, obj):
        if obj.average_rating is None:
            return "No data"

        return obj.average_rating
        

class ActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        exclude = ('id',)

class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ('id', 'color')

class FilmDetailSerializer(serializers.ModelSerializer):
    actors = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()
    banner = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    
    class Meta:
        model = Film
        fields = ('title', 'year', 'description', 'average_rating', 'banner', 'genres', 'actors')

    def get_actors(self, obj):
        if obj.actors.all().exists():
            response = ActorsSerializer(read_only = True, many = True, instance = obj.actors)
            return response.data
        
        return "No data"

    def get_genres(self, obj):
        if obj.genres.all().exists():
            response = GenresSerializer(read_only = True, many = True, instance = obj.genres)
            return response.data
        
        return "No data"

    def get_banner(self, obj):
        return f"{settings.HOST}{obj.banner.url}"

    def get_average_rating(self, obj):
        if obj.average_rating is None:
            return "No data"

        return obj.average_rating