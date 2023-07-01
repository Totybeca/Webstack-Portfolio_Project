from django import forms
from .models import CustomUser

class SignUpForm(forms.ModelForm):
    username = forms.CharField(
        label='Username',
        max_length=150,
        help_text='',
        validators=[],
        widget=forms.TextInput(attrs={'autocomplete': 'off'})
    )
    
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'subject']

