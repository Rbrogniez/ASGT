# Generated by Django 4.1.6 on 2023-02-12 16:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0017_alter_games_created_at_alter_tournament_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 12, 16, 35, 8, 858629, tzinfo=datetime.timezone.utc), verbose_name='Ajouté le'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 12, 16, 35, 8, 858917, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 12, 16, 35, 8, 858444, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
    ]
