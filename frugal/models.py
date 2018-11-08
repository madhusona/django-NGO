from django.db import models

# Create your models here.

from django.db import models
from django.forms import ModelForm
from django import forms
from datetime import datetime
from django.core.exceptions import ValidationError
import re


# Create your models here.
class NGO(models.Model):
    Organization_Name = models.CharField(max_length=200,help_text="Maximum 200 Characters")
    Contact_Person = models.CharField(max_length=50,help_text="Maximum 50 Characters")
    Email_id = models.CharField(max_length=50,primary_key=True,help_text="Maximum 50 Characters")
    Mobile_no = models.CharField(max_length=10,help_text="Should be 10 Characters")
    Address   =   models.CharField(null=True,blank=True,max_length=200,help_text="Door No and Street. Maximum 200 Characters")
    City = models.CharField(max_length=50,help_text="Maximum 50 Characters")
    Latitude = models.DecimalField(null=True,blank=True,max_digits=13, decimal_places=10)
    Longitude = models.DecimalField(null=True,blank=True,max_digits=13, decimal_places=10)
    Pincode = models.CharField(max_length=6,help_text="Should be 6 Characters")
    Website = models.CharField(max_length=30,blank=True,null=True,help_text="Maximum 30 Characters")
    Established_on = models.DateField(help_text="Required.")

    def __str__(self):
          return self.Email_id


    
class NGO_Profile(models.Model):
    NGO = models.OneToOneField(NGO,on_delete=models.CASCADE)
    Overview = models.CharField(max_length=10000,help_text="About your Organization")
    Cover_Photo = models.ImageField(upload_to = 'pictures',null=True, blank=True)
    Account_STATUS = (
        ('R', 'Registered'),
        ('V', 'Verified'),
        ('A', 'Activated'),
        ('D', 'Deactivated'),
    )

    Status = models.CharField(max_length=1,choices=Account_STATUS,default='R')

class NGO_Registration(models.Model):
    NGO = models.ForeignKey(NGO,on_delete=models.CASCADE)
    Recognized_Body = models.CharField(max_length=100)
    Registration_Number = models.CharField(max_length=100)



     
class SignupForm(ModelForm):
    class Meta:
        model=NGO
        fields=['Organization_Name','Contact_Person','Email_id','Mobile_no','City','Pincode','Website','Established_on']
        widgets = {
            'Address': forms.Textarea, 'Email_id':forms.EmailInput,'Established_on':forms.SelectDateWidget(years=range(1900,datetime.today().year+1))
        }
    def clean_Mobile_no(self):
        data = self.cleaned_data['Mobile_no']
        
        if len(data) != 10 or not data.isdigit():
            raise ValidationError('Invalid Mobile No')
        return data
    def clean_Pincode(self):
        data = self.cleaned_data['Pincode']
        
        if len(data) != 6 or not data.isdigit():
            raise ValidationError('Invalid Pincode')
        return data

    def clean_Email_id(self):
        data = self.cleaned_data['Email_id']
        if NGO.objects.filter(Email_id=self.cleaned_data['Email_id']).exists():
            raise ValidationError('Email ID already Exsists')
        return data

class ProfileForm(forms.Form):
    Overview = forms.CharField(widget=forms.Textarea)
    Cover_Photo = forms.ImageField()

class NGO_locationForm(forms.Form):
    Address = forms.CharField(widget = forms.Textarea)
    City = forms.CharField(widget = forms.HiddenInput(attrs={'readonly':'readonly'}))
    latitude = forms.DecimalField(widget = forms.HiddenInput(attrs={'readonly':'readonly'}))
    longitude = forms.DecimalField(widget = forms.HiddenInput(attrs={'readonly':'readonly'}))

    



   






      


