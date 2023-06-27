from django.urls import path
from ElectronicWebAPI.views import signup

urlpatterns = [
    path('signup/', signup, name='signup'),
]