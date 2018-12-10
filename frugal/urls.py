from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Registration/',views.register,name='register'),
    path('Profile/',views.Profile,name='Profile'),
    path('Map/',views.Map,name='Map'),
    path('Ngo_Donation/',views.Ngo_Donation, name='Ngo_Donation'),
    path('Open_Donation/',views.Open_Donation,name="Open_Donation"),
    path('Ngo_Accepted/',views.Ngo_Accepted,name="Ngo_Accepted"),
    path('Ngo_Received/',views.Ngo_Received,name="Ngo_Received"),
    path('Edit_Activity/',views.Edit_Activity,name="Edit_Activity"),
    path('Edit_Need/',views.Edit_Need,name="Edit_Need"),
    path('Donor_Register/',views.Donor_Register,name="Donor_Register"),
    path('Donate/',views.Donate,name="Donate"),
    path('My_Donation/',views.My_Donaton,name='My_Donation'),

]