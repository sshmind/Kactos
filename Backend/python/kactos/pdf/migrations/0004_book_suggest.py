# Generated by Django 3.0.3 on 2020-03-08 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0003_genre_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='suggest',
            field=models.BooleanField(default=False),
        ),
    ]
