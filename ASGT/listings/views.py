from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Tournament

def hello(request):
    tournament = Tournament.objects.all()
    return HttpResponse(f"""<h1>Hello Django!</h1>
    <p>Liste des jeux disponibles</p>
    <ul>
        <li>{tournament[0].name}</li>
        <li>{tournament[1].name}</li>
        <li>{tournament[2].name}</li>
    </ul>
    """)

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>test ASGT</p>')

def listings(request):
    return HttpResponse('<h1>Liste des jeux</h1> <p>Vous trouverez ici tous les jeux actuellement disponibles')

def contact(request):
    return HttpResponse("<h1>Contact</h1> <p>Si vous avez une question, un retour, ou toute autre demande, n'hésitez pas à contacter l'équipe ASGT")