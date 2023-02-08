from django.db import models
from django.core.validators import MinValueValidator

# Si nous souhaitez créer un objet (ou un champ) dans une BDD, toujours faire hériter de models.Model
# listings/models.py

class Games(models.Model):
    name = models.fields.CharField(max_length=100)

class Tournament(models.Model):
    name = models.fields.CharField(max_length=100)

class User(models.Model):
    username = models.fields.CharField(max_length=25)

class Round(models.Model):
    round_number = models.IntegerField(MinValueValidator(1))