from django.urls import path
from django.views.decorators.cache import never_cache
from debug_toolbar.views import render_panel

from . import views

app_name = 'ElectronicWebAPI'

urlpatterns = [
    path('render_panel/', never_cache(render_panel), name='render_panel'),
    path('register/', views.register_view, name='register'),
    path('base/', views.base_view, name='base'),
    path('home/', views.home_view, name='home'),
    path('about/', views.about_view, name='about_us'),
    path('contact', views.contact_view, name='contact_us'),
    path('product/', views.product_view, name='our_product'),
    path('categories/', views.categories_view, name='all_categories'),
]