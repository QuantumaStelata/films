# Generated by Django 3.2.8 on 2021-10-22 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_alter_rating_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='average_rating',
            field=models.FloatField(blank=True, default=1, verbose_name='Средняя оценка'),
            preserve_default=False,
        ),
    ]
