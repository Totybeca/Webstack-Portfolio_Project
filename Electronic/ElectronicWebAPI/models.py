from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import TextInput

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200, default='default_value')
    last_name = models.CharField(max_length=200, default='default_value')
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200, unique=True)
    email = models.EmailField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
        verbose_name='Email',
        help_text='Please enter your email'
        )
    subject = models.CharField(max_length=200, default='default_value')

    
    class Meta:
        swappable = 'AUTH_USER_MODEL'
    
    # CustomUser._meta.get_field('groups').remote_field.related_name = 'customuser_set'
    # CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'customuser_set'
