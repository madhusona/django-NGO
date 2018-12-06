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
    path('Edit_Service/',views.Edit_Service,name="Edit_Service"),
    path('Edit_Activity/',views.Edit_Activity,name="Edit_Activity"),
    path('Edit_Need/',views.Edit_Need,name="Edit_Need"),

]