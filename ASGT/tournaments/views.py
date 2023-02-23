from django.http import HttpResponse
from django.shortcuts import render, redirect
from tournaments.models import Tournament, User, Games
from tournaments.forms import ContactUsForm, TournamentForm
from django.core.mail import send_mail
from django.http import JsonResponse
import json

def homepage(request):
    user = User.objects.all()
    return render(request, 'tournaments/homepage.html', {'users': user})

def games(request):
    games = Games.objects.all()
    return render(request, 'tournaments/games.html', {'games': games})

def about(request):
    return render(request, 'tournaments/about-us.html')

def tournament(request):
    tournaments = Tournament.objects.all()
    return render(request, 'tournaments/tournaments.html', {'tournaments': tournaments})

def contact(request):

    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message de {form.cleaned_data["name"]} d\'ASGT - formulaire de contact',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['axel.gore@outlook.fr']
        )
        return redirect('/confirmation-contact')
    else:
        form = ContactUsForm()
    
    return render(request, 'tournaments/contact.html', {'form': form})

def contact_ok(request):
    return render(request, 'tournaments/contact-ok.html')

def tournament_detail(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)

    return render (request, 'tournaments/tournament_detail.html', {'tournament': tournament})

def tournament_create(request):
    if request.method == 'POST':
        tournament_form = TournamentForm(request.POST)
        if tournament_form.is_valid():
            tournament_form = tournament_form.save()
            return redirect('tournament-detail', tournament_form.id)
    else:
        tournament_form = TournamentForm()

    return render(request, 'tournaments/tournament-creation.html', {'form': tournament_form})

def tournament_update(request, tournament_id):

    tournament = Tournament.objects.get(id=tournament_id)

    if request.method == 'POST':
        tournament_form = TournamentForm(instance=tournament)
        if tournament_form.is_valid():
            tournament_form.save()
            return redirect('tournament-detail', tournament.id)
    else:
        tournament_form = TournamentForm(instance=tournament)
    return render(request, 'tournaments/tournament-update.html', {'tournament_form': tournament_form})

def tournament_delete(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    return render(request, 'tournaments/tournament_delete.html', {'tournament': tournament})