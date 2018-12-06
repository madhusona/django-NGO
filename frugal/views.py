from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from .models import NGO_Profile
from .models import NGO
from .models import NGO_Registration



# Create your views here.
def index(request):
    return render(request,'frugal/index.html')

def Edit_Need(request):
    form=models.Need_Form()
    return render(request,'frugal/Edit_Need.html',{'form':form})

def Edit_Activity(request):
    form=models.Activity_Form()
    return render(request,'frugal/Edit_Activity.html',{'form':form})

def Edit_Service(request):
    return render(request,'frugal/Edit_service.html')

def Ngo_Donation(request):
    form = models.Ngo_home()
    return render(request,'frugal/Ngo_home.html',{'form':form})
#   return render(request,'frugal/index.html')
def Open_Donation(request):
    form = models.Ngo_home()
    return render(request,'frugal/Ngo_bid.html',{'form':form})

def Ngo_Accepted(request):
     return render(request,'frugal/Ngo_accepted.html')



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
            request.session['pincode']=str(form.cleaned_data['Pincode'])
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
            Record.Pincode = str(request.session['pincode'])
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


   



