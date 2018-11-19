from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models


# Create your views here.
def index(request):
    return render(request,'frugal/index.html')

def register(request):
    args = {}
    if request.method == 'POST':
        form = models.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = models.SignupForm()
    args['form'] = form
    return render(request, 'frugal/Register.html', {'form': form}) 
   



