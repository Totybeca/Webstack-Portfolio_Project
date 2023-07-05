from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import SESSION_KEY, authenticate, login
from django.contrib.auth.models import User, auth
from django.conf import settings as app_settings
from django.views import View

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


# Using the long-required decorator
@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')


# Using the anonymous required decorator
@anonymous_required
def login(request):
    context = {"Message": 'Successful'}
    return render(request, 'login.html', context)
    
  
@anonymous_required
def register(request):
    context = {"Message": 'Successful'}
    return render(request, 'register.html', context)


@login_required
def dashboard(request):
    context = {"Message": 'Successful'}
    return render(request, 'dashboard.html', context)




def about(request):
    return render(request, 'about.html')


def product(request):
    return render(request, 'product.html')


def contact(request):
    return render(request, 'contact.html')


# def phones(request):
#     return render(request, 'phones.html')


# def computers(request):
#     return render(request, 'computers.html')


# def conditioners(request):
#     return render(request, 'conditioners.html')


# def air_pods(request):
#     return render(request, 'air_pods.html')


# def watches(request):
#     return render(request, 'watches.html')


# def head_phones(request):
#     return render(request, 'head_phones.html')


# def washing_machines(request):
#     return render(request, 'washing_machines.html')


# def monitors(request):
#     return render(request, 'monitors.html')


def services(request):
    return render(request, 'services.html')


def terms(request):
    return render(request, 'terms.html')


def privacy(request):
    return render(request, 'privacy.html')
