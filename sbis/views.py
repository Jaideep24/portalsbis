from ast import For
from dataclasses import fields
from re import template
from urllib import request
from django.shortcuts import render
import requests
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
# Create your views here.
students_list=[]#for list of students
teachers_list=[]
mydict={"teacher":teachers.objects.all().values(),"students":students.objects.all().values(),"student_name":"","form":Form.objects.all().values(),"teacher_data":every_teacher.objects.all().values(),"teacher_name":""}
#to check which teacher or student of which class is viewing/editing a model and assign model to class view accordingly
def home(request):
    global student_form
    global teacher_name
    global mydict
    #print(teachers.objects.all().values())
    for i in students.objects.all().values():
        students_list.append(i["name"])
    for k in teachers.objects.all().values():
        teachers_list.append(k["name"])
    #print(mydict)
    if "input" in request.POST:
        if request.POST["input"] in students_list:
            mydict["student_name"]=request.POST["input"]
            return (render(request,"sbis/home.html",mydict))
        elif request.POST["input"]in teachers_list:
            mydict["teacher_name"]=request.POST["input"]
            return (render(request,"sbis/teacher.html",mydict))
        else:
            return (render(request,"sbis/login.html",mydict))
    else:
        return (render(request,"sbis/login.html",mydict))
def worksheet(request):
    return(render(request,"sbis/view_worksheets.html",mydict))
def circular(request):
    return(render(request,"sbis/circular.html",mydict))
class circular_form(CreateView):
    model=Form
    template_name="sbis/circular_form.html"
    fields=["circular_title","circular","circular_pdf","form"]
    success_url="/"
class submit_form(CreateView):
    model=every_teacher
    fields=["student_name","teacher_name","work_pdf"]
    template_name="sbis/upload.html"
    success_url="/"
class worksheet_form(CreateView):
    model=Form
    template_name="sbis/worksheet_form.html"
    fields=["worksheet_title","worksheet","worksheet_pdf","form"]
    success_url="/"