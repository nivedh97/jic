from django import forms

# Create your forms here.
from django.forms import ModelForm
from .models import JobApplication

class AppForm(ModelForm):
     class Meta:
         model = JobApplication
         fields ="__all__"
         
class ContactForm(forms.Form):
    name = forms.CharField(max_length = 50)
    email= forms.EmailField(max_length = 150)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)
    subject= forms.EmailField(max_length = 150)

class ApplyJobForm(forms.Form):
    name = forms.CharField(max_length = 50)
    email= forms.EmailField(max_length = 150)
    mobile= forms.CharField(max_length = 50)
    resume = forms.FileField()


