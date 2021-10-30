from django.test import TestCase

from apps.database.models import Film, Actor, Genre, Comment, Rating
from django.urls import reverse
# Create your tests here.

class MainTest(TestCase):

    def setUp(self):
        self.film = Film.objects.create(title = 'Film', banner = 'film/banner.jpg', year = 2000, description = 'Film Description')
        self.actor = Actor.objects.create(name = 'Actor name', surname = 'Actor surname')
        self.genre = Genre.objects.create(title = 'Genre')

        self.film.actors.add(self.actor)
        self.film.genres.add(self.genre)

    def test_main_view(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_main_view_by_name(self):
        resp = self.client.get(reverse('main'))
        self.assertEqual(resp.status_code, 200)


    def test_film_view(self):
        resp = self.client.get('/film/1')
        self.assertEqual(resp.status_code, 200)

    def test_film_view_by_name(self):
        resp = self.client.get(reverse('film', args=(1,)))
        self.assertEqual(resp.status_code, 200)

    
    def test_genre_view(self):
        resp = self.client.get('/genre/1')
        self.assertEqual(resp.status_code, 200)

    def test_genre_view_by_name(self):
        resp = self.client.get(reverse('genre', args=(1,)))
        self.assertEqual(resp.status_code, 200)


    def test_actor_view(self):
        resp = self.client.get('/actor/1')
        self.assertEqual(resp.status_code, 200)

    def test_actor_view_by_name(self):
        resp = self.client.get(reverse('actor', args=(1,)))
        self.assertEqual(resp.status_code, 200)
        