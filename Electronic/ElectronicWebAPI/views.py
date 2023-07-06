from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import SESSION_KEY, authenticate, login
from django.contrib.auth.models import User, auth
from django.conf import settings as app_settings
from django.views import View
from django.core.mail import send_mail
from .forms import LoginForm, RegisterForm, ContactForm
from .models import Contact
from django.http import JsonResponse


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
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard') # redirect to dashboard after successful login
        else:
            error = "Invalid username or password."
            error = None
            context = {'form': form, 'error': error}
            return render(request, 'login.html', context)
    
    
  
@anonymous_required
def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('login')
    context = {'form': form}
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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            
            # Create and save the Contact instance
            contact = Contact(name=name, email=email, phone_number=phone_number, message=message)
            contact.save()
            
            # Perform additional actions
            # For example, send an email
            send_email(name, email, phone_number, message)
            
            # Redirect or render a success message
            contact_success = "Successful!"
            return render(request, contact_success)
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


def send_email(name, email, phone_number, message):
    subject = 'New Contact Form Submission'
    body = f'''
        Name: {name}
        Email: {email}
        Phone Number: {phone_number}
        Message: {message}
    '''
    sender = 'your-email@example.com'
    recipient = 'recipient@example.com'
    
    send_mail(subject, body, sender, [recipient])

def _header(request):
    dropdown_items = [
        "Mobile phones",
        "Computers",
        "Air Conditioners",
        "AirPods",
        "Smart Watches",
        "Headphones",
        "Washing Machines",
        "PC Monitors",
    ]
    context = {'dropdown_items': dropdown_items}
    return render(request, 'partials/_header.html', context)



def search(request):
    search_term = request.GET.get('search_term')
    
    # Perform search logic and retrieve search results
    
    # Return search results as JSON response
    return JsonResponse(search_results)







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
