from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.core.mail import send_mail
from home.models import Project,Services,About
from smtplib import SMTP
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    sk = About.objects.all()
    context = {'sk':sk}
    return render(request,'about.html',context)

def projects(request):
    proj = Project.objects.all()
    context = {'proj':proj}
    return render(request,'projects.html', context)


def resume(request):
    return render(request,'resume.html')

def services(request):
    ser = Services.objects.all()
    context = {'ser':ser}
    return render(request,'services.html',context)



def WhatsappData(sub):
    import time 
    import webbrowser as web
    import pyautogui as pg
    # print("Im here")
    web.open_new_tab('https://web.whatsapp.com/send?phone=917666794499'+'&text='+sub)
    time.sleep(30)
    pg.press('enter')


def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

        sub = "Name: " + name + "\n" + "Email: " + email + "\n\n\n" + "Message: " + message

        print(sub )
        # url = 'https://web.whatsapp.com/send?phone=917666794499'+'&text='+sub
        # web.open(url)
        # return redirect(url)
        WhatsappData(sub)
        

        # #send mail
        messages.success(request, "Thank You" )

        # send_mail(
        #    subject,#suject 
        #    sub,#msg
        #    email, #from 
        #    ['pushks7777@gmail.com'], #to

        # )


        # print(name, email , subject , message )
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        # print("the db is updated")
    return render(request,'contact.html')