from django import forms
from tournaments.models import Tournament

class ContactUsForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(max_length=500)

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['tournament_name', 'nb_players', 'game',
                  'player1', 'player2', 'player3', 'player4',
                  'player5', 'player6', 'player7', 'player8',
                  'start_date', 'start_time']