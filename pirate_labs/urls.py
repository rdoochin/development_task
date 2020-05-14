from django.contrib import admin
from django.urls import path, include
from user import views as user_views
# Used for the login page.
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls, name ='admin'),
    path('register/', user_views.register, name='register'),
    # Calls the django-defined login page. 
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('welcome/', user_views.welcome, name='welcome'),
    path('', include('user.urls')),
]
