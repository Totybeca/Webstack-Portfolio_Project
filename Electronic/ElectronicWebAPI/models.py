from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django import forms


class CustomUserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email, password=None):
        if not username:
            raise ValueError("The username field must be set")
        if not email:
            raise ValueError("The email field must be set")
        
        email = self.normalize_email(email)
        user = self.model(username=username, first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, first_name, last_name, email, password=None):
        user = self.create_user(username, first_name, last_name, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'password']
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
    
    def has_module_perms(self, app_label):
        return self.is_staff
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name