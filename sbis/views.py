from django.shortcuts import render
import requests
from .models import *
# Create your views here.
students_list=[]
def home(request):
    #print(teachers.objects.all().values())
    for i in students.objects.all().values():
        students_list.append(i["name"])
    print(request.POST)
    mydict={"teacher":teachers.objects.all().values()}
    print(mydict)
    if "input" in request.POST:
        if request.POST["input"] in students_list:
            return (render(request,"sbis/home.html",mydict))
        else:
            return (render(request,"sbis/login.html",mydict))
    else:
        return (render(request,"sbis/home.html",mydict))
def teacher(request):
    return(render(request,"sbis/teacher.html"))
def worksheet(request):
    return(render(request,"sbis/worksheet.html"))
def circular(request):
    return(render(request,"sbis/circular.html"))
def upload(request):
    return(render(request,"sbis/upload.html"))