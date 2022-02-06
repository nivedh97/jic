from django.shortcuts import render
from .models import Careers
# Create your views here.
from django.http import HttpResponse
import json 
from .templates import *
# Create your views here.
def careers(request): 
    careers= Careers.objects.all()
    print(careers)
    services=[]
    return render(request,'careers.html',{"services":services,"careers":careers})
