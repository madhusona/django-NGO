from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Registration/',views.register,name='register'),
<<<<<<< HEAD
=======
    path('Profile/',views.Profile,name='Profile'),
    path('Map/',views.Map,name='Map')
    
>>>>>>> e8d80d4f45b62e55e361be0b15a59de3c6ce12e9
]