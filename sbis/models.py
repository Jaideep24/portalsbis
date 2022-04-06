from operator import mod
from statistics import mode
from xml.parsers.expat import model
from django.db import models

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=20, blank=True)
    middle_name=models.CharField(max_length=10, blank=True)
    surname=models.CharField(max_length=10, blank=True)
    form=models.CharField(max_length=10, blank=True)
    roll_no=models.IntegerField()
    contact_number=models.IntegerField()
    def __str__(self):
        return (self.name)
class Form(models.Model):
    teachers=models.CharField(max_length=20, blank=True)
    circular_title=models.CharField(max_length=30, blank=True)
    circular=models.CharField(max_length=100, blank=True)
    circular_pdf=models.FileField(blank=True)
    worksheet_title=models.CharField(max_length=30, blank=True)
    worksheet=models.CharField(max_length=100, blank=True)
    worksheet_pdf=models.FileField(blank=True)
    form=models.CharField(max_length=4,blank=True, default=None)
    def __str__(self) -> str:
        return (self.circular_title)
class teachers(models.Model):
    name=models.CharField(max_length=20, blank=True)
    middle_name=models.CharField(max_length=10, blank=True)
    surname=models.CharField(max_length=10, blank=True)
    form=models.CharField(max_length=10, blank=True)
    subject1=models.CharField(max_length=100, blank=True)
    subject2=models.CharField(max_length=100,blank=True)
    contact_number=models.IntegerField()
    def __str__(self):
        return (self.name)
class every_teacher(models.Model):
    student_name=models.ForeignKey(students,on_delete=models.CASCADE)
    teacher_name=models.ForeignKey(teachers,on_delete=models.CASCADE,blank=True,default=None)
    work_pdf=models.FileField(blank=True)
    def __str__(self):
        return (self.teacher_name)