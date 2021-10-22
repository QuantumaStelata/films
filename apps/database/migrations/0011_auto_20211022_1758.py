# Generated by Django 3.2.8 on 2021-10-22 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_auto_20211022_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='average_rating',
            field=models.FloatField(blank=True, max_length=3, null=True, verbose_name='Средняя оценка'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='grade',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], verbose_name='Оценка'),
        ),
    ]
