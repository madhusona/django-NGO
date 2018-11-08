from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Registration/',views.register,name='register'),
    path('Profile/',views.Profile,name='Profile'),
    path('Map/',views.Map,name='Map')
    
]