from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'average_rating', 'date_create')
    readonly_fields = ('average_rating', 'date_create')
    filter_horizontal = ('actors', 'genres')
    search_fields = ('title', 'genres__title', 'actors__name', 'actors__surname')
    list_filter = ('genres__title',)

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')
    search_fields = ('name', 'surname')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title', 'color')
    search_fields = ('title',)
    ordering = ('title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('film', 'ip', 'date_create')
    search_fields = ('film__title', )
    list_filter = ('date_create',)
    
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('film', 'ip', 'grade')
    search_fields = ('film__title', 'ip', 'grade')
    list_filter = ('grade',)

