from django.urls import path
from . import views

urlpatterns = [
    # Directs the local host to the registration page. 
    path('', views.register, name = 'user-registration'),
]