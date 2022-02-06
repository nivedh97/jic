from django.db import models

# Create your models here.
class Careers(models.Model):  
    title = models.CharField(max_length=50, help_text='Career Name')
    experience = models.CharField(max_length=50, help_text='Career Name')
    Details = models.CharField(max_length=1000)
    