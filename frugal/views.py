<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse
=======
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from .models import NGO_Profile
from .models import NGO
from .models import NGO_Registration

>>>>>>> e8d80d4f45b62e55e361be0b15a59de3c6ce12e9


# Create your views here.
def index(request):
    return render(request,'frugal/index.html')

<<<<<<< HEAD
def register(request):
    return HttpResponse("Hello, world. You're at the polls index.")
#   return render(request,'frugal/index.html')
=======

def register(request):
    #args = {}
    if request.method == 'POST':
        form = models.SignupForm(request.POST)
        if form.is_valid():
            request.session['step1_form']=request.POST
            request.session['city'] = form.cleaned_data['City']
            return redirect('Map')
    else:
        form = models.SignupForm()
    #args['form'] = form
    return render(request, 'frugal/Register.html', {'form': form})

def Map(request):
    if request.method == 'POST':
        form = models.NGO_locationForm(request.POST, request.FILES)
        if form.is_valid():
            request.session['latitude']=float(form.cleaned_data['latitude'])
            request.session['longitude']=float(form.cleaned_data['longitude'])
            request.session['address']=str(form.cleaned_data['Address'])
            return redirect('Profile')
    else:
        form=models.NGO_locationForm()
        form.fields["City"].initial = request.session['city']
    
    return render(request,'frugal/map.html',{'form':form})

def Profile(request):
    if request.method == 'POST':
        form = models.ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            reg_form= models.SignupForm(request.session['step1_form'])
            reg_form.save()
           
            Record = NGO.objects.get(Email_id=reg_form.cleaned_data['Email_id'])
            Record.Latitude = float(request.session['latitude'])
            Record.Longitude = float(request.session['longitude'])
            Record.Address = str(request.session['address'])
            Record.save()
            profile = NGO_Profile()
            profile.NGO=NGO.objects.get(Email_id=reg_form.cleaned_data['Email_id'])
            profile.Overview = form.cleaned_data['Overview']
            profile.Cover_Photo = form.cleaned_data['Cover_Photo']
            profile.Status ='R'
            profile.save()

                
            for count in range(1,4):
                field1="Recognized_Body"+str(count)
                if request.POST.get(field1)!=None:
                    registration1=NGO_Registration()
                    registration1.NGO=NGO.objects.get(Email_id=reg_form.cleaned_data['Email_id'])
                    registration1.Recognized_Body=request.POST.get("Recognized_Body"+str(count))
                    registration1.Registration_Number=request.POST.get("Registration_Number"+str(count))
                    registration1.save()
                 
            del request.session['step1_form']
            return redirect('index')
    else:
        form=models.ProfileForm()        
    return render(request, 'frugal/Profile.html',{'form': form})


   
>>>>>>> e8d80d4f45b62e55e361be0b15a59de3c6ce12e9



