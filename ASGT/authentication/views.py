from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import forms

def logout_user(request):
    logout(request)
    return redirect('homepage')

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else :
                message = 'Identifiants invalides.'
                
    return render(request, 'authentication/login.html', context={'form': form, 'message': message})

