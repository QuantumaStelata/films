# Generated by Django 3.2.8 on 2021-10-22 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0014_auto_20211022_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='Жанр'),
        ),
    ]