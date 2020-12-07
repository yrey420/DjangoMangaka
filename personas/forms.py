from django import forms
from django.contrib.auth.forms import UserCreationForm
from personas.models import LocalUser


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your Username",
                "class": "form-control"
            }
        ))

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter your password",
                "class": "form-control"

            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your new username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter your e-Mail",
                "class": "form-control"

            }
        ))

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter your new password",
                "class": "form-control"

            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Let's double check your password",
                "class": "form-control"
            }
        ))

    class Meta:
        model = LocalUser
        fields = ('username', 'email', 'password1', 'password2')
