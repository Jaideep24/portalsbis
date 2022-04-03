from dataclasses import fields
from re import template
from django.shortcuts import render
import requests
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
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
        return (render(request,"sbis/login.html",mydict))
def teacher(request):
    return(render(request,"sbis/teacher.html"))
def worksheet(request):
    return(render(request,"sbis/worksheet.html"))
def circular(request):
    return(render(request,"sbis/circular.html"))
def upload(request):
    return(render(request,"sbis/upload.html"))
class submit_form(CreateView):
    model=every_teacher
    fields=["student_name","work_pdf"]
    template_name="sbis/upload.html"
class Worksheet_list(ListView):
    model=Form1
    template_name="sbis/view_worksheets.html"