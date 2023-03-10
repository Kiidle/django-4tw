from django import forms
from django.forms import ModelForm
from authentication.models import User


class SignUpForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name', 'last_name', "username", 'birthdate', 'email', 'password']
        labels = {
            "first_name": "Vorname",
            "last_name": "Nachname",
            "username": "Benutzername",
            "birthdate": "Geburtsdatum",
            "email": "E-Mail Adresse",
            "password": "Passwort"
        }
        help_texts = {
            "username": ""
        }
        error_messages = {
            'name': {
                "required": "Pflichtfeld"
            }
        }

    def save(self, commit=True):
        user = super().save(commit=commit)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
