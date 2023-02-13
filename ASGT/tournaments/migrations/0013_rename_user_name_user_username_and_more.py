# Generated by Django 4.1.6 on 2023-02-12 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0012_remove_user_tournament_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_name',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='tournament',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 12, 15, 55, 44, 89867, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 12, 15, 55, 44, 90197, tzinfo=datetime.timezone.utc)),
        ),
    ]
