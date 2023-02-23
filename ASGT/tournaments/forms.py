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

"""
class TournamentScoreFormRound1(forms.Form):
    scoreP1 = forms.IntegerField(label='', required=True)
    scoreP2 = forms.IntegerField(label='', required=True)
    scoreP3 = forms.IntegerField(label='', required=True)
    scoreP4 = forms.IntegerField(label='', required=True)
    scoreP5 = forms.IntegerField(label='', required=True)
    scoreP6 = forms.IntegerField(label='', required=True)
    scoreP7 = forms.IntegerField(label='', required=True)
    scoreP8 = forms.IntegerField(label='', required=True)

class TournamentScoreFormRound2(forms.Form):
    scoreP1 = forms.IntegerField(label='', required=True)
    scoreP2 = forms.IntegerField(label='', required=True)
    scoreP3 = forms.IntegerField(label='', required=True)
    scoreP4 = forms.IntegerField(label='', required=True)

class TournamentScoreFormFinale(forms.Form):
    scoreP1 = forms.IntegerField(label='', required=True)
    scoreP2 = forms.IntegerField(label='', required=True)

class MatchForm(forms.Form):
    scoreP1 = forms.IntegerField(label='Test', required=True)
    scoreP2 = forms.IntegerField(label='Test', required=True)
"""