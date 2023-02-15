from django.http import HttpResponse
from django.shortcuts import render
from tournaments.models import Tournament, User, Games
from tournaments.forms import ContactUsForm

def homepage(request):
    user = User.objects.all()
    return render(request, 'tournaments/homepage.html', {'users': user})

def games(request):
    games = Games.objects.all()
    return render(request, 'tournaments/games.html', {'games': games})

def about(request):
    return render(request, 'tournaments/about-us.html')

def tournament(request):
    tournament = Tournament.objects.all()
    return render(request, 'tournaments/tournaments.html', {'tournaments': tournament})

def contact(request):
    form = ContactUsForm()
    return render(request, 'tournaments/contact.html', {'form': form})

def tournament_detail(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    return render (request, 'tournaments/tournament_detail.html', {'tournament': tournament})
