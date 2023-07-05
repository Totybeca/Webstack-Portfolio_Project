from django.urls import path
from . import views


urlpatterns = [
    path('', views.register, name="register"),
    #path('base', views.base, name="base"),
    path('', views.about, name="about"),
    path('', views.contact, name="contact"),
    path('', views.product, name="product"),
    # path('categories', views.categories, name="all_categories"),
    path('', views.login, name="login"),
    path('', views.dashboard, name="dashboard"),
    path('', views.phones, name="phones"),
    path('', views.computers, name="computers"),
    path('', views.conditioners, name="conditioners"),
    path('', views.air_pods, name="air_pods"),
    path('', views.watches, name="watches"),
    path('', views.head_phones, name="head_phones"),
    path('', views.washing_machines, name="washing_machines"),
    path('', views.monitors, name="monitors"),
]
