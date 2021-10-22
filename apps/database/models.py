from django.db import models

from .validators import photo_validator

class Film(models.Model):
    title = models.CharField(verbose_name = 'Название', max_length = 255)
    photo = models.FileField(verbose_name = 'Баннер', upload_to = 'films/', validators = [photo_validator])
    description = models.TextField(verbose_name = 'Описание')
    actors = models.ManyToManyField('Actor', verbose_name = 'Фильмы', related_name = 'films', blank = True)
    genres = models.ManyToManyField('Genre', verbose_name = 'Жанры', related_name = 'films', blank = True)

    average_rating = models.FloatField(verbose_name = 'Средняя оценка', blank = True, null = True)

    def __str__(self):
        return self.title

class Actor(models.Model):
    name = models.CharField(verbose_name = 'Имя', max_length = 255)
    surname = models.CharField(verbose_name = 'Фамилия', max_length = 255)

    def __str__(self):
        return f"{self.name} {self.surname}"
        
class Genre(models.Model):
    title = models.CharField(verbose_name = 'Жанр', max_length = 50, unique = True)
    color = models.CharField(verbose_name = 'Цвет', max_length = 7, default = '#FFFFFF')

    def __str__(self):
        return self.title
        

class Comment(models.Model):
    film = models.ForeignKey('Film', verbose_name = 'Фильм', related_name = 'comments', on_delete = models.CASCADE)
    name = models.CharField(verbose_name = 'Имя', max_length = 255)
    text = models.CharField(verbose_name = 'Текст', max_length = 255)
    ip = models.GenericIPAddressField(verbose_name = 'IP отправителя')
    date_create = models.DateTimeField(verbose_name = 'Время создания', auto_now_add = True)

    def __str__(self):
        return f"{self.film} - {self.ip}"

class Rating(models.Model):
    GRADES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
              (6, 6), (7, 7), (8, 8), (9, 9), (10, 10))


    film = models.ForeignKey('Film', verbose_name = 'Фильм', on_delete = models.CASCADE, related_name = 'grades')
    grade = models.IntegerField(verbose_name = 'Оценка', choices = GRADES)
    ip = models.GenericIPAddressField(verbose_name = 'IP отправителя')

    class Meta:
        unique_together = ('film', 'ip')

    def __str__(self):
        return f"{self.ip} - {self.grade}"

    def save(self, *args, **kwargs):
        super().save()
        self.update_average_rating()

    def update_average_rating(self):
        grades = [grade.grade for grade in self.film.grades.all()]
        average_rating = round(sum(grades) / len(grades), 2)
        self.film.average_rating = average_rating
        self.film.save()
        
        
        
