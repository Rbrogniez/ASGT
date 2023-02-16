import random
from django.db import models
from tournaments.models import Tournament




class player_number_attrib():
    list_players = models.ForeignKey(Tournament.player1)
    print(list_players)

if __name__=="__main__":
        player_number_attrib()
        print(player_number_attrib)