from django.shortcuts import render, redirect
from .forms import SignUpForm

def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Display a success message
            message = 'Sign-up successful. Please log in.'
            return render(request, 'templates/success.html', {'message': message})
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def base_view(request):
    return render(request, 'base.html')
def home_view(request):
    return render(request, 'home.html')
def about_view(request):
    return render(request, 'about.html')
def contact_view(request):
    return render(request, 'contact.html')
def product_view(request):
    return render(request, 'product.html')
def categories_view(request):
    return render(request, 'categories.html')