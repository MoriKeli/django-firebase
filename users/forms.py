from django.contrib.auth.forms import AuthenticationForm
from django import forms


class UserLoginForm(AuthenticationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'type': 'email'}), required=True)
    password = forms.CharField(widget=forms.TextInput(attrs={'type': 'password'}), required=True)
    