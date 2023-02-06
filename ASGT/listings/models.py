from django.db import models

# Si nous souhaitez créer un objet (ou un champ) dans une BDD, toujours faire hériter de models.Model
# listings/models.py

class Games(models.Model):
    name = models.fields.CharField(max_length=100)
