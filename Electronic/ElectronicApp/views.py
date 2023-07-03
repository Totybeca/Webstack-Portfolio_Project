from django.shortcuts import redirect, render

def home(request):
    auth.login(request)
    return redirect('login')
    