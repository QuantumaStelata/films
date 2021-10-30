from django.test import TestCase
import json
from django.urls.base import reverse

from apps.database.models import Film, Actor, Genre, Rating, Comment

from django.contrib.auth.models import User
from django.test.client import Client
# Create your tests here.

class ApiTest(TestCase):

    def setUp(self):
        self.film = Film.objects.create(title = 'Film', banner = 'film/banner.jpg', year = 2000, description = 'Film Description')
        self.actor = Actor.objects.create(name = 'Actor name', surname = 'Actor surname')
        self.genre = Genre.objects.create(title = 'Genre')

        self.film.actors.add(self.actor)
        self.film.genres.add(self.genre)

        my_admin = User.objects.create_superuser('admin', 'myemail@test.com', 'admin')
        self.client = Client()
        self.client.login(username=my_admin.username, password='admin')


    def test_api(self):
        resp = self.client.get('/api/')
        self.assertEqual(resp.status_code, 200)

    def test_api_by_name(self):
        resp = self.client.get(reverse('api'))
        self.assertEqual(resp.status_code, 200)

    def test_api_context(self):
        resp = self.client.get(reverse('api'))
        content = json.loads(resp.content)
        self.assertEqual(len(content), 5)

    def test_api_ratings(self):
        data = {'id': 1, 'grade': 10}
        resp = self.client.post(reverse('api-rating'), data = data)
        content = json.loads(resp.content)
        self.assertEqual(resp.status_code, 200)

    def test_api_comment(self):
        data = {'id': 1, 'name': 'name', 'text': 'text'}
        resp = self.client.post(reverse('api-comment'), data = data)
        content = json.loads(resp.content)
        self.assertEqual(resp.status_code, 200)
