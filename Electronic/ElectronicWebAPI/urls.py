from django.urls import path
from . import views


urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('product', views.product, name="product"),
    #path('base', views.base, name="base"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('services',views.services, name="services"),
    path('terms', views.terms, name="terms"),
    path('privacy', views.privacy, name="privacy"),
    path('_header', views._header, name="_header"),
   
]
     
     
#     
#    
     
    #path('phones', views.phones, name="phones"),
#     path('computers', views.computers, name="computers"),
#     path('conditioners', views.conditioners, name="conditioners"),
#     path('air_pods', views.air_pods, name="air_pods"),
#     path('watches', views.watches, name="watches"),
#     path('head_phones', views.head_phones, name="head_phones"),
#     path('washing_machines', views.washing_machines, name="washing_machines"),
#     path('monitors', views.monitors, name="monitors"),
#    
#     
 #]
