# Generated by Django 4.0.2 on 2022-02-22 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='budget',
            field=models.IntegerField(default=100000),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
