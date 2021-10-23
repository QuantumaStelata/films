from rest_framework import serializers

from apps.database.models import Film, Actor, Genre

from django.conf import settings

class ActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        exclude = ('id',)

class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ('id', 'color')

class FilmsSerializer(serializers.ModelSerializer):
    actors = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = Film
        fields = ('url', 'title', 'year', 'description', 'average_rating', 'photo', 'genres', 'actors')

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

    def get_photo(self, obj):
        return f"{settings.HOST}{obj.photo.url}"

    def get_average_rating(self, obj):
        if obj.average_rating is None:
            return "No data"

        return obj.average_rating

    def get_url(self, obj):
        return f"{settings.HOST}/api/films/{obj.id}"
        


# class UrlDetailSerializer(serializers.ModelSerializer):
#     visitors = serializers.SerializerMethodField()

#     class Meta:
#         model = Url
#         exclude = ('is_delete', 'creator_user', 'creator_ip')

#     def get_visitors(self, obj):
#         return obj.visitors.count()