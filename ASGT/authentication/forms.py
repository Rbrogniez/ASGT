from django import forms

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
