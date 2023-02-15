from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Si nous souhaitez créer un objet (ou un champ) dans une BDD, toujours faire hériter de models.Model
# tournaments/models.py

class User(models.Model):
    
    def __str__(self):
        return f'{self.username}' #permet d'afficher directement le username dans l'administration Django plutôt qu'un nom d'objet + id

    username = models.fields.CharField(max_length=30)
    created_at = models.fields.DateTimeField(
        default=timezone.now(),
        verbose_name='Créé le'
        )
    updated_at = models.fields.DateTimeField(
        auto_now=True,
        verbose_name='Modifié le'
        )
    email = models.fields.EmailField(
        blank=True,
        null=True
        )
    password = models.fields.CharField(
        max_length=25,
        blank=True,
        null=True
        )

class Games(models.Model):

    def __str__(self):
        return f'{self.game_name}'
    
    game_name = models.fields.CharField(max_length=100)
    created_at = models.fields.DateTimeField(
        default=timezone.now(),
        verbose_name = 'Ajouté le'
        )

class Tournament(models.Model):

    def __str__(self):
        return f'{self.tournament_name}'

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
    created_at = models.fields.DateTimeField(
        default=timezone.now(),
        verbose_name="Créé le"
        ) 
    updated_at = models.fields.DateTimeField(auto_now=True)
    nb_players = models.fields.IntegerField(validators=
        [MinValueValidator(8, "Le nombre de participants est imposé à 8 pour le moment"), 
        MaxValueValidator(8, "Le nombre de participants est imposé à 8 pour le moment")],
        verbose_name="Nombre de participants",
        blank=True,
        null=True
        )
    game = models.ForeignKey(
        Games,
        on_delete=models.SET_NULL, 
        verbose_name='Jeu',
        blank=True,
        null=True
        )
    admin = models.fields.CharField(max_length=20, 
        default=''
        ) #user_id de l'admin
    player1 = models.ForeignKey(
        User, 
        null=True, 
        on_delete=models.SET_NULL, #set_null car si on utilise CASCADE ça supprimera tout le tournoi
        verbose_name="Joueur 1",
        related_name='+'
        )
    player2 = models.ForeignKey(
        User, 
        null=True, 
        on_delete=models.SET_NULL, 
        verbose_name="Joueur 2",
        related_name='+'
        )
    player3 = models.ForeignKey(
        User, 
        null=True, 
        on_delete=models.SET_NULL, 
        verbose_name="Joueur 3",
        related_name='+'
        )
    player4 = models.ForeignKey(
        User, 
        null=True, 
        on_delete=models.SET_NULL, 
        verbose_name="Joueur 4",
        related_name='+'
        )
    player5 = models.ForeignKey(
        User, 
        null=True, 
        on_delete=models.SET_NULL, 
        verbose_name="Joueur 5",
        related_name='+'
        )
    player6 = models.ForeignKey(
        User, 
        null=True, 
        on_delete=models.SET_NULL, 
        verbose_name="Joueur 6",
        related_name='+'
        )
    player7 = models.ForeignKey(
        User, 
        null=True, 
        on_delete=models.SET_NULL, 
        verbose_name="Joueur 7",
        related_name='+'
        )
    player8 = models.ForeignKey(
        User, 
        null=True, 
        on_delete=models.SET_NULL, 
        verbose_name="Joueur 8",
        related_name='+'
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



