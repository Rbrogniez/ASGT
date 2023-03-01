from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez le Nom d\'utilisateur',
        }),
        label='Nom d\'utilisateur',
        required=True,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez l\'adresse e-mail',
        }),
        label='Adresse e-mail',
        required=True,
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez le Mot de passe',
        }),
        label='Mot de passe',
        required=True,
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmez le Mot de passe',
        }),
        label='Confirmez le Mot de passe',
        required=True,
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Entrez le Nom d\'utilisateur'
        }),
        label='Nom d\'utilisateur'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Entrez le Mot de passe'
        }),
        label='Mot de passe'
    )

