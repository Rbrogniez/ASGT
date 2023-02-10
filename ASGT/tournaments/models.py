from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Si nous souhaitez créer un objet (ou un champ) dans une BDD, toujours faire hériter de models.Model
# tournaments/models.py

class Games(models.Model):
    
    game_name = models.fields.CharField(max_length=100)

class Tournament(models.Model):

    class Games_choices(models.TextChoices):
        FIFA = 'FIFA'
        SSBU = 'Super Smash Bros Ultimate'
        DBFZ = 'Dragon Ball FighterZ'

    tournament_name = models.fields.CharField(
        max_length=100,
        verbose_name="Nom du tournoi",
        blank=True,
        null=True
        )
    created_at = models.fields.DateTimeField(default=timezone.now()) 
    updated_at = models.fields.DateTimeField(auto_now=True)
    nb_players = models.fields.IntegerField(validators=
        [MinValueValidator(8, "Le nombre de participants est imposé à 8 pour le moment"), 
        MaxValueValidator(8, "Le nombre de participants est imposé à 8 pour le moment")],
        verbose_name="Nombre de participants",
        blank=True,
        null=True
        )
    game = models.fields.CharField(
        choices=Games_choices.choices, 
        max_length=50,
        verbose_name='Jeu',
        blank=True,
        null=True
        )
    admin = models.fields.CharField(max_length=20, 
        default='Test'
        ) #user_id de l'admin
    player1 = models.fields.CharField(
        verbose_name="Joueur 1",
        max_length=20,
        blank=True,
        null=True
        )
    player2 = models.fields.CharField(
        verbose_name="Joueur 2",
        max_length=20,
        default="Bot"
        )
    player3 = models.fields.CharField(
        verbose_name="Joueur 3",
        max_length=20,
        blank=True,
        null=True
        )
    player4 = models.fields.CharField(
        verbose_name="Joueur 4",
        max_length=20,
        blank=True,
        null=True
        )
    player5 = models.fields.CharField(
        verbose_name="Joueur 5",
        max_length=20,
        blank=True,
        null=True
        )
    player6 = models.fields.CharField(
        verbose_name="Joueur 6",
        max_length=20,
        blank=True,
        null=True
        )
    player7 = models.fields.CharField(
        verbose_name="Joueur 7",
        max_length=20,
        blank=True,
        null=True
        )
    player8 = models.fields.CharField(
        verbose_name="Joueur 8",
        max_length=20,
        blank=True,
        null=True
        )
    start_date = models.fields.DateField(
        verbose_name="Date de début",
        blank=True,
        null=True
        )
    start_time = models.fields.TimeField(
        verbose_name="Date de début",
        blank=True,
        null=True
        )
    tournament_infos = models.JSONField(
        blank=True,
        null=True
        )


class User(models.Model):
    user_name = models.fields.CharField(max_length=30)
    created_at = models.fields.DateTimeField(default=timezone.now())
    updated_at = models.fields.DateTimeField(auto_now=True)
    tournament_id = models.fields.CharField(
        max_length=20,
        blank=True,
        null=True
        )
    email = models.fields.EmailField(
        "Saisissez une adresse courriel valide",
        blank=True,
        null=True
        )
    password = models.fields.CharField(
        max_length=25,
        blank=True,
        null=True
        )
