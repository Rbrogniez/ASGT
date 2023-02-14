from django.http import HttpResponse
from django.shortcuts import render
from tournaments.models import Tournament, User, Games

def homepage(request):
    user = User.objects.all()
    return render(request, 'tournaments/homepage.html', {'users': user})

def games(request):
    games = Games.objects.all()
    return render(request, 'tournaments/games.html', {'games': games})

def about(request):
    return render(request, 'tournaments/about-us.html')

def tournament(request):
    return render(request, 'tournaments/tournaments.html')

def contact(request):
    return render(request, 'tournaments/contact.html')

def tournament_detail(request, id):
    return render (request, 'tournaments/tournament_detail.html', {'id': id})