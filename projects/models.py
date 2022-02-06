from django.db import models

# Create your models here.
class ProjectDetails(models.Model):  
    title = models.CharField(max_length=50, )
    owned_by = models.CharField(max_length=50,)
    project_value = models.CharField(max_length=1000)
    scope = models.CharField(max_length=1000)
    role= models.CharField(max_length=1000)
    ongoing = models.BooleanField()
    project_image=models.ImageField(upload_to ='uploads/project/',null = True)
    owner_logo=models.ImageField(upload_to ='uploads/project/',null = True)