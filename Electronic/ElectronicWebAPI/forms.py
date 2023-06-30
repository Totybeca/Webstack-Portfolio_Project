from django import forms
from .models import CustomUser

class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = '__all__'
