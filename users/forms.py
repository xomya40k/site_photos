from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User
from django import forms

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'type':'text',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'type': 'password',
        'placeholder': 'Password',
    }))

    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'placeholder': 'Username',
        'autocomplete': 'username',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'type': 'email',
        'placeholder': 'Email',
        'autocomplete': 'email',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'type': 'password',
        'placeholder': 'Password',
        'autocomplete': 'new-password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'type': 'password',
        'placeholder': 'Confirm password',
        'autocomplete': 'new-password',
    }))

    class Meta:
        model = User
        fields = ('username', 'email' ,'password1', 'password2')