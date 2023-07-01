from django.urls import path
from django.views.decorators.cache import never_cache
from debug_toolbar.views import render_panel
import debug_toolbar
from . import views
from .views import CustomUserAPIView
from .views import LoginFormView
from django.contrib.auth.views import LoginView

app_name = 'ElectronicWebAPI'

urlpatterns = [
    path('render_panel/', never_cache(render_panel), name='render_panel'),
    path('users/', CustomUserAPIView.as_view(), name='custom_users'),
    path('register/', views.register, name='register'),
    path('base/', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about_us'),
    path('contact/', views.contact, name='contact_us'),
    path('product/', views.product, name='our_product'),
    path('categories/', views.categories, name='all_categories'),
   path('login/', LoginView.as_view(template_name='login.html'), name='login'),
]
