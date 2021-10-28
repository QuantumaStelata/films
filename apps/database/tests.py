from datetime import timedelta
from django.test import TestCase

from .models import Film, Actor, Genre, Comment, Rating

# Create your tests here.

class DataBaseTest(TestCase):

    def setUp(self):
        self.film = Film.objects.create(title = 'Film', banner = 'img/photo.jpg', year = 2000, description = 'desc', film = 'film/film.mp4')

    def test_add_genre(self):
        self.genre = Genre.objects.create(title = 'Genre')
        self.film.genres.add(self.genre)
        self.assertIn(self.genre, self.film.genres.all())

    def test_add_actor(self):
        self.actor = Actor.objects.create(name = 'Actor', surname = 'SurActor')
        self.film.actors.add(self.actor)
        self.assertIn(self.actor, self.film.actors.all())

    def test_add_comment(self):
        self.comment = Comment.objects.create(film = self.film, name = 'name', text = 'text', ip = '127.0.0.1')
        self.assertIn(self.comment, self.film.comments.all())

    def test_add_rating(self):
        GRADE = 5

        self.rating = Rating.objects.create(film = self.film, grade = GRADE, ip = '127.0.0.1')
        self.assertIn(self.rating, self.film.grades.all())
        self.assertEqual(self.film.average_rating, GRADE)
        self.assertEqual(self.film.grades.count(), 1)

        self.rating.delete()
        self.assertEqual(self.film.average_rating, None)
        self.assertEqual(self.film.grades.count(), 0)

    
