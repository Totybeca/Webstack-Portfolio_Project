from django.urls import path
from ElectronicWebAPI.views import signup

app_name = 'djdt'

urlpatterns = [
    path('signup/', signup, name='signup'),
]