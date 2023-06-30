from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'templates/register.html', {'form': form})

def base(request):
    return render(request, './templates/base.html')
def home(request):
    return render(request, './templates/home.html')
def about_us(request):
    return render(request, './templates/about_us.html')
def contact_us(request):
    return render(request, './templates/contact_us.html')
def our_product(request):
    return render(request, './templates/our_product.html')
def all_categories(request):
    return render(request, './templates/all_categories.html')
def _header(request):
    return render(request, './templates/partials/_header.html')
def _footer(request):
    return render(request, './templates/partials/_footer.html')