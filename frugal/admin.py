from django.contrib import admin
from .models import NGO,NGO_Profile,NGO_Registration

# Register your models here.
admin.site.register(NGO)
admin.site.register(NGO_Profile)
admin.site.register(NGO_Registration)
