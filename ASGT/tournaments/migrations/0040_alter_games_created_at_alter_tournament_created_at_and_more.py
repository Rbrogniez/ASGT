# Generated by Django 4.1.7 on 2023-03-01 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0039_alter_games_created_at_alter_tournament_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 1, 10, 36, 46, 833654, tzinfo=datetime.timezone.utc), verbose_name='Ajouté le'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 1, 10, 36, 46, 833933, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 1, 10, 36, 46, 833468, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
    ]
