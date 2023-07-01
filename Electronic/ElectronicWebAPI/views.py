from django.shortcuts import render, redirect
from .forms import SignUpForm
from rest_framework import status
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from django.views import View
from .models import CustomUser
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm

# Create views here

class CustomUserAPIView(View):
    def get(self, request):
        custom_users = CustomUser.objects.all()
        serializer = CustomUserSerializer(custom_users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Display a success message
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')  # Redirect to the login page
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

class LoginFormView(LoginView):
    template_name = 'login.html'  # Path to your login template
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')  # URL to redirect after successful login


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