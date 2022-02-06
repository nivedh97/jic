from django.shortcuts import render 
from .models import *
from home.models import Services
# Create your views here.
def projects(request):
    projects = ProjectDetails.objects.all()
    services = Services.objects.all()
    return render(request,'projects.html',{"projects":projects,"services":services})