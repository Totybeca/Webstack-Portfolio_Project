from django.urls import path
from . import views


urlpatterns = [
    path('register', views.register, name="register"),
    # path('base', views.base, name="base"),
    # path('about', views.about, name="about_us"),
    # path('contact', views.contact, name="contact_us"),
    # path('product', views.product, name="our_product"),
    # path('categories', views.categories, name="all_categories"),
    path('login', views.login, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
   
]
