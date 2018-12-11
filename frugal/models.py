from django.db import models

# Create your models here.

from django.db import models
from django.forms import ModelForm
from django import forms
from datetime import datetime
from django.core.exceptions import ValidationError

import re


# Create your models here.

"""Declare models for YOUR_APP app."""

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    
class NGO(models.Model):
    Organization_Name = models.CharField(max_length=200,help_text="Maximum 200 Characters")
    Contact_Person = models.CharField(max_length=50,help_text="Maximum 50 Characters")
    Email_id = models.CharField(max_length=50,primary_key=True,help_text="Maximum 50 Characters")
    Mobile_no = models.CharField(max_length=10,help_text="Should be 10 Characters")
    Address   =   models.CharField(null=True,blank=True,max_length=200)
    City = models.CharField(max_length=50,help_text="Maximum 50 Characters")
    Latitude = models.DecimalField(null=True,blank=True,max_digits=13, decimal_places=10)
    Longitude = models.DecimalField(null=True,blank=True,max_digits=13, decimal_places=10)
    Pincode = models.CharField(null=True,max_length=6,help_text="Should be 6 Characters")
    Website = models.CharField(max_length=30,blank=True,null=True,help_text="Maximum 30 Characters")
    Established_on = models.DateField(help_text="Required.")

    def __str__(self):
          return self.Email_id


    
class NGO_Profile(models.Model):
    NGO = models.OneToOneField(NGO,on_delete=models.CASCADE)
    Overview = models.CharField(max_length=10000,help_text="About your Organization")
    Cover_Photo = models.ImageField(upload_to = 'frugal/static/frugal/images/Cover_photo',null=True, blank=True)
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

class Ngo_Activity(models.Model):
    NGO = models.ForeignKey(NGO,on_delete=models.CASCADE)
    Title = models.CharField(max_length=30)
    Detail = models.CharField(max_length=200)
    Photo = models.ImageField(upload_to = 'frugal/static/frugal/images/Activity')
    Date = models.DateField()

class Services(models.Model):
    Service_Name = models.CharField(primary_key=True,max_length=20)

class Category(models.Model):
    Category_Name = models.CharField(primary_key=True,max_length=30)
    Credit_Point = models.IntegerField()

class Product(models.Model):
    Product_Name = models.CharField(primary_key=True,max_length=30)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)


class Ngo_Need(models.Model):
    NGO = models.ForeignKey(NGO,on_delete=models.CASCADE)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    Count = models.IntegerField()
    Detail = models.CharField(max_length=1000)
    Sample_Photo = models.ImageField(upload_to = 'frugal/static/frugal/images/Need')
    Need_Option = (('O','One Time Need'),('L','Life Time Need'))
    Need_Category = models.CharField(max_length=1,choices=Need_Option,default='O')
    Need_Status = (('O','Opened'),('C','Closed'))
    Status = models.CharField(max_length=1,choices=Need_Status,default='O')
    Date = models.DateField(auto_now_add=True)

class Donor(models.Model):
    Donor_Name = models.CharField(max_length=50,help_text="Maximum 50 Characters")
    DOB = models.DateField(help_text="Required.")
    Email_id = models.CharField(max_length=50,primary_key=True,help_text="Maximum 50 Characters")
    Mobile_no = models.CharField(max_length=10,help_text="Should be 10 Characters")
    Profile_Photo = models.ImageField(upload_to = 'frugal/static/frugal/images/Profile_Photo',null=True, blank=True)
    Address   =   models.CharField(null=True,blank=True,max_length=200)
    City = models.CharField(max_length=50,help_text="Maximum 50 Characters")
    Pincode = models.CharField(null=True,max_length=6,help_text="Should be 6 Characters")
    Latitude = models.DecimalField(null=True,blank=True,max_digits=13, decimal_places=10)
    Longitude = models.DecimalField(null=True,blank=True,max_digits=13, decimal_places=10)


class Donation_Interest(models.Model):
    Donor = models.ForeignKey(Donor,on_delete=models.CASCADE)
    Ngo_Need = models.ForeignKey(Ngo_Need, on_delete=models.CASCADE)
    Count = models.IntegerField()
    Product_Photo = models.ImageField(upload_to = 'frugal/static/frugal/images/Requests',null=True, blank=True)
    Interest_Status = (('P','Posted'),('A','Accepted'),('D','Declined'))
    Status = models.CharField(max_length=1,choices=Interest_Status, default='P')
    Date = models.DateField(auto_now_add=True)

class Donations(models.Model):
    NGO = models.ForeignKey(NGO,on_delete=models.CASCADE)
    Donor = models.ForeignKey(Donor,on_delete=models.CASCADE)
    Product_Name = models.ForeignKey(Product,on_delete=models.CASCADE)
    Count = models.IntegerField()
    Donated_Photo = models.ImageField(upload_to = 'frugal/static/frugal/images/Donations',null=True, blank=True)
    Date = models.DateField(auto_now_add=True)

class Post_Donation(models.Model):
    Donor = models.ForeignKey(Donor,on_delete=models.CASCADE)
    Product_Name = models.ForeignKey(Product,on_delete=models.CASCADE)
    Count = models.IntegerField()
    Detail = models.CharField(max_length=1000)
    Product_Photo = models.ImageField(upload_to = 'frugal/static/frugal/images/Requests',null=True, blank=True)
    Post_Status = (('P','Posted'),('C','Closed'))
    Status = models.CharField(max_length=1,choices=Post_Status, default='P')
    Date = models.DateField(auto_now_add=True)
    End_Date = models.DateField()

class Post_Cause(models.Model):
    Post_Donation = models.ForeignKey(Post_Donation,on_delete=models.CASCADE)
    Service = models.ForeignKey(Services,on_delete=models.CASCADE)

class NGO_Bid(models.Model):
    Post_Donation = models.ForeignKey(Post_Donation,on_delete=models.CASCADE)
    NGO = models.ForeignKey(NGO,on_delete=models.CASCADE)
    Count = models.IntegerField()
    Date = models.DateField(auto_now_add=True)
    Bid_Status = (('R','Requested'),('A','Accepted'),('C','Closed'))
    Status = models.CharField(max_length=1,choices=Bid_Status, default='R')

class Interest_Decline(models.Model):
    Donation_Interest = models.ForeignKey(Donation_Interest,on_delete=models.CASCADE)
    Declined_Reason = (('N','Not Needed Now'),('L','Donor Location is too Long'),('D','Product Damaged'),('O','Others'))
    Reason = models.CharField(max_length=1,choices= Declined_Reason, default='N')
    Comments = models.CharField(max_length=200,null=True,blank=True)




class SignupForm(ModelForm):
    
    class Meta:
        model=NGO
        fields=['Organization_Name','Contact_Person','Email_id','Mobile_no','City','Website','Established_on']
        widgets = {
            'Address': forms.Textarea, 'Email_id':forms.EmailInput,'Established_on':forms.SelectDateWidget(years=range(1900,datetime.today().year+1))
        }

    

    def clean_Mobile_no(self):
        data = self.cleaned_data['Mobile_no']
        
        if len(data) != 10 or not data.isdigit():
            raise ValidationError('Invalid Mobile No')
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
    Pincode = forms.CharField(required=True)
    City = forms.CharField(widget = forms.HiddenInput(attrs={'readonly':'readonly'}))
    latitude = forms.DecimalField(required=True,widget = forms.HiddenInput(attrs={'readonly':'readonly'}))
    longitude = forms.DecimalField(required=True,widget = forms.HiddenInput(attrs={'readonly':'readonly'}))
    map_click = forms.CharField(required=False,widget = forms.HiddenInput(attrs={'readonly':'readonly'}))

    def clean_Pincode(self):
        data = self.cleaned_data['Pincode']
        
        if len(data) != 6 or not data.isdigit():
            raise ValidationError('Invalid Pincode')
        return data

    def clean_map_click(self):
        data = self.cleaned_data['map_click']
        if data != "True":
            raise ValidationError('Locate You in Google Maps')

        return data

class Ngo_home(forms.Form):
    Location_Choices = ((500,'All'),(2,'Less than 2Kms'),(5,'Less than 5kms'),(20,'Less than 20kms'),(100,'Less than 100kms'))
    Category = (('All','All'),('Furniture','Furniture'),('Books','Books'),('Clothes','Clothes'),('Home applicences','Home applicences'))

    Location = forms.CharField(widget=(forms.Select(choices=Location_Choices)))
    Category = forms.CharField(widget=(forms.Select(choices=Category)))

class Activity_Form(ModelForm):
    class Meta:
        model=Ngo_Activity
        fields=['Title','Detail','Photo','Date']
        widgets = {
            'Detail': forms.Textarea,'Date':forms.SelectDateWidget(years=range(2000,datetime.today().year+1))
        }
class Need_Form(ModelForm):
   
    class Meta:
        
        model = Ngo_Need
        fields=['Category','Product', 'Count', 'Detail', 'Sample_Photo','Need_Category']
        widgets = {
            
            'Detail': forms.Textarea
        }

class Donor_Reg_Form(ModelForm):
    class Meta:
        model=Donor
        fields=['Donor_Name','DOB','Email_id','Mobile_no','Profile_Photo','City','Address','Pincode','Latitude','Longitude']
        widgets = {
            'Address': forms.Textarea, 'Email_id':forms.EmailInput,'DOB':forms.SelectDateWidget(years=range(datetime.today().year-100,datetime.today().year+1)),
            'Latitude': forms.HiddenInput(attrs={'readonly':'readonly'}),
            'Longitude' : forms.HiddenInput(attrs={'readonly':'readonly'})
        }

class Donation_Form(forms.Form):
    Category = forms.ModelChoiceField(queryset=Category.objects.all().order_by('Category_Name'))
    Product_Name = forms.ModelChoiceField(queryset=Product.objects.all().order_by('Product_Name'))
    Count = forms.IntegerField(widget=(forms.NumberInput()))
    Product_Photo = forms.ImageField()

class Cause_Form(forms.Form):
    Cause = forms.ModelChoiceField(widget=forms.SelectMultiple(),queryset=Services.objects.all().order_by('Service_Name'))


class Post_Donation_Form(forms.Form):
    End_Date = forms.DateField(widget=forms.SelectDateWidget(years=range(datetime.today().year,datetime.today().year+2)))
    Cause = forms.ModelChoiceField(widget=forms.SelectMultiple(),queryset=Services.objects.all().order_by('Service_Name'))

class Decline_Form(ModelForm):
    class Meta:
        model=Interest_Decline
        fields=['Reason','Comments']
        widgets = {
            'Comments': forms.Textarea
         }

   










    



   






      


