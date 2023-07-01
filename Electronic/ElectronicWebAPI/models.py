from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, default='')
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name='Email',
        help_text='Please enter your email'
    )
    subject = models.CharField(max_length=200, default='')

    class Meta:
        swappable = 'AUTH_USER_MODEL'
