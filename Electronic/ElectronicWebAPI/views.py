from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.conf import settings
from django.utils import timezone
from random import randint
from django.contrib import messages
from django.contrib.auth import SESSION_KEY, authenticate, login
from django.contrib.auth.models import user, auth

# Create views here

def anonymous_required(function=None, redirect_url=None):
    
   if not redirect_url:
       redirect_url = 'dashboard'

   actual_decorator = user_passes_test(
       lambda u: u.is_anonymous,
       login_url=redirect_url
   )

   if function:
       return actual_decorator(function)
   return actual_decorator




#using the long-required decorator
@login_required
def logout(request):
  auth.logout(request)
  return redirect('login')




#using the anonymous required decorator
@anonymous_required
def login(request):
    context = {"Message": 'Successful'}
    return render(request, 'login', context)
    
    
    
  
@anonymous_required
def register(request):
    context = {"Message": 'Successful'}
    return render(request, 'login', context)

@login_required
def dashboard(request):
    context = {"Message": 'Successful'}
    return render(request, 'dashboard', context)







def base(request):
    return render(request, 'base.html')
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def product(request):
    return render(request, 'product.html')
def categories(request):
    return render(request, 'categories.html')