from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    
    class Meta:
        swappable = 'AUTH_USER_MODEL'
    
    # CustomUser._meta.get_field('groups').remote_field.related_name = 'customuser_set'
    # CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'customuser_set'
