
from django.db import models
from django.forms import ModelForm
from django import forms
from datetime import datetime
# Create your models here.
class NGO(models.Model):
     Organization_Name = models.CharField(max_length=200,help_text="Required. Maximum 200 Characters")
     Contact_Person = models.CharField(max_length=50,help_text="Required. Maximum 50 Characters")
     Email_id = models.CharField(max_length=50,help_text="Required. Maximum 50 Characters")
     Mobile_no = models.CharField(max_length=10,help_text="Required. Maximum 10 Characters")
     Address   =   models.CharField(max_length=200,help_text="Required. Door No and Street. Maximum 200 Characters")
     City = models.CharField(max_length=50,help_text="Required. Maximum 50 Characters")
     Pincode = models.CharField(max_length=6,help_text="Required. Maximum 6 Characters")
     Website = models.CharField(max_length=30,null=True,help_text="Optional. Maximum 30 Characters")
     Established_on = models.DateField(help_text="Required.")
     
class SignupForm(ModelForm):
    class Meta:
        model=NGO
        fields=['Organization_Name','Contact_Person','Email_id','Mobile_no','Address','City','Pincode','Website','Established_on']
        widgets = {
            'Address': forms.Textarea, 'Email_id':forms.EmailInput,'Established_on':forms.SelectDateWidget(years=range(1900,datetime.today().year+1))
        }
    def clean(self):
        data = self.cleaned_data
        if len(data['Mobile_no']) != 10:
            raise forms.ValidationError('Mobile Number Should be 10 Digits!!!')
        if len(data['Pincode']) != 6:
            raise forms.ValidationError('Pincode Should be 6 Digits!!!')
        return self.cleaned_data




      


