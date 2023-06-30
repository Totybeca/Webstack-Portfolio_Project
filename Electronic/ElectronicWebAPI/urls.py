from django.urls import path
from . import views

app_name = 'djdt'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('base/', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('our_product/', views.our_product, name='our_product'),
    path('all_categories/', views.all_categories, name='all_categories'),
    path('_footer/', views._footer, name='_footer'),
    path('_header/', views._header, name='_header'),
]