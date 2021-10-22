from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title',)
    readonly_fields = ('average_rating',)
    filter_horizontal = ('actors', 'genres')

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title', 'color')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('film', 'ip', 'date_create')
    
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('film', 'ip', 'grade')


