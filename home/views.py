from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def projects(request):
    return render(request,'projects.html')


def resume(request):
    return render(request,'resume.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        print(name, email , subject , message )
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        print("the db is updated")
    return render(request,'contact.html')