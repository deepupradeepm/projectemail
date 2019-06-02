from django.core.mail import send_mail
from django.shortcuts import render

import app1
from app1.models import Student_Modle
from projectmailpasssend2 import settings


def autogenid():
    qs=Student_Modle.objects.all()
    if qs:
        return qs[len(qs)-1].idno+1
    else:
        idno=101
        return idno
def saved(req):
  if req.method=="POST":
    idno=req.POST.get("id")
    name=req.POST.get("name")
    cno=req.POST.get("cno")
    gender=req.POST.get("gender")
    image=req.POST.get("image")
    email=req.POST.get("email")
    pword=req.POST.get("password")
    pword1=req.POST.get("password1")
    if pword==pword1:
        Student_Modle(idno=idno,name=name,cno=cno,gender=gender,image=image,email=email,password=pword).save()
        send_mail("sathya tech","student details are saved ",settings.EMAIL_HOST_USER,[email])
        return render(req,"register.html",{"message":"data is inserted in database"})
    else:
        return render(req, "index.html", {"message": "data is not inserted in database"})



def register(req):
    idno=autogenid()
    return render(req,"register.html",{"auto_id":idno})


def validation(req):
    email=req.POST.get("email")
    pword=req.POST.get("password")
    try:
       object=Student_Modle.objects.get(email=email)
       if object.password==pword:
           return render(req,"studnt.html")
       else:
           return render(req,"login.html",{"message":"invalid password"})
    except app1.models.Student_Modle.DoesNotExist:
        return render(req,"login.html",{"message":"username is invalid"})

    return None