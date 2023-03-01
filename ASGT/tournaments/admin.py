from django.contrib import admin

from tournaments.models import User, Games, Tournament


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'email', 'created_at')

class GamesAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'id', 'created_at')

class TournamentAdmin(admin.ModelAdmin):
    list_display = ('tournament_name', 'id', 'game', 'admin', 'nb_players', 'player1', 'player2',
    'player3', 'player4', 'player5', 'player6', 'player7', 'player8', 'created_at', 'updated_at',
    'start_date', 'start_time', 'tournament_infos'
    )


admin.site.register(User, UserAdmin)
admin.site.register(Games, GamesAdmin)
admin.site.register(Tournament, TournamentAdmin)

