from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=100)
    subject = forms.CharField(max_length=200)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'password', 'email', 'subject')
