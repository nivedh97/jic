from career.models import *
from django.db import models 
from django.core.validators import FileExtensionValidator
class Contact(models.Model):  
    name = models.CharField(max_length=50,)
    email = models.EmailField(max_length=50, )
    subject = models.CharField(max_length=1000)
    message = models.CharField(max_length=1000)

class Services(models.Model):  
    name = models.CharField(max_length=50) 
    details = models.CharField(max_length=1000) 

class JobApplication(models.Model):  
    name = models.CharField(max_length=50, )
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=50, )
    resume =models.FileField(upload_to ='uploads/resume/',validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    career = models.ForeignKey(to=Careers,on_delete=models.CASCADE)
