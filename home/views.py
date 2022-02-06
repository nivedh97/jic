from django.shortcuts import render
from .models import *
from career.models import *
from projects.models import ProjectDetails
from .forms import *
from django.http import HttpResponse
import json 
# Create your views here.
def home3(request):
    services = Services.objects.all()
    clients= ProjectDetails.objects.all()
    print(clients)
    return render(request,'index.html',{"services":services,"clients":clients})

def contact(request):
    services = Services.objects.all()
    careers= Careers.objects.all()
    print(careers)
    title=""
    return render(request,'contact.html',{"services":services,"careers":careers,"title":title})

def aboutus(request):  
    return render(request,'about.html')

def services(request):  
    services = Services.objects.all()
    return render(request,'services.html',{"services":services})

def contactform(request):
    if request.method == 'POST':
        print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
			'name': form.cleaned_data['name'],  
			'email': form.cleaned_data['email'],
            'sunject': form.cleaned_data['sunject'],
			'message':form.cleaned_data['message'], 
			}
            message = "\n".join(body.values())
            # try:
            #     send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            # except BadHeaderError:
			# 	return HttpResponse('Invalid header found.')
			# return redirect ("main:homepage")
            contact = Contact.objects.create(name=body["name"],email=body["email"],message=body["message"],subject=body["subject"])
            print("contact",contact)
            contact.save() 
    form = ContactForm()
    response_data={"success":True}
    return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

def CarrerApply(request,id=None):
    services = Services.objects.all()
    careers= Careers.objects.get(id=id)
    jobs = JobApplication.objects.all()
    print(jobs)
    print(careers)
    return render(request,'CareerApply.html',{"services":services,"careers":careers})

def UploadResume(request,id=None):
    if request.method == 'POST': 
        form = AppForm(request.POST, request.FILES)
        print(request.POST)
        career = Careers.objects.filter(id=id)
        if form.is_valid() and career.exists(): 
            body = {
			'name': form.cleaned_data['name'],  
			'email': form.cleaned_data['email'], 
			'mobile':form.cleaned_data['mobile'],  
			}
            message = "\n".join(body.values())
            # try:
            #     send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            # except BadHeaderError:
			# 	return HttpResponse('Invalid header found.')
			# return redirect ("main:homepage")
            jobApplications = JobApplication.objects.create(name=body["name"],email=body["email"],mobile=body["mobile"],resume=request.FILES['resume'],career=career[0])
            print("JobApplication",JobApplication)
            jobApplications.save()
            response_data={"success":True}
        else:
            print(form.errors)
            response_data={"success":False,"message":form.errors}

    form = ApplyJobForm() 
    return HttpResponse(
            json.dumps(response_data),
            content_type="application/json",
        )
