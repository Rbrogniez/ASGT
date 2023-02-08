from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Tournament, User, Games

def hello(request):
    user = User.objects.all()
    return render(request, 'listings/hello.html', {'users': user})

def games(request):
    games = Games.objects.all()
    return render(request, 'listings/games.html', {'games': games})

def about(request):
    return render(request, 'listings/about-us.html')

def listings(request):
    return HttpResponse('<h1>Liste des jeux</h1> <p>Vous trouverez ici tous les jeux actuellement disponibles')

def contact(request):
    return HttpResponse("<h1>Contact</h1> <p>Si vous avez une question, un retour, ou toute autre demande, n'hésitez pas à contacter l'équipe ASGT")