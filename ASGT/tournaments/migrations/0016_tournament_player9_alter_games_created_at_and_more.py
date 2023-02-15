# Generated by Django 4.1.6 on 2023-02-12 16:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0015_games_created_at_alter_tournament_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='player9',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tournaments.user', verbose_name='Joueur 1'),
        ),
        migrations.AlterField(
            model_name='games',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 12, 16, 26, 19, 907368, tzinfo=datetime.timezone.utc), verbose_name='Ajouté le'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 12, 16, 26, 19, 907611, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 12, 16, 26, 19, 907153, tzinfo=datetime.timezone.utc), verbose_name='Créé le'),
        ),
    ]
