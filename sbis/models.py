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
    circular_pdf=models.FileField()
    worksheet_title=models.CharField(max_length=30, blank=True)
    worksheet=models.CharField(max_length=100, blank=True)
    worksheet_pdf=models.FileField()
class Form1(Form):
    def __str__(self):
        return (self.circular_title)
class Form2(Form):
    def __str__(self):
        return (self.circular_title)
class Form3(Form):
    def __str__(self):
        return (self.circular_title)
class Form4(Form):
    def __str__(self):
        return (self.circular_title)
class Form5(Form):
    def __str__(self):
        return (self.circular_title)
class Form6(Form):
    def __str__(self):
        return (self.circular_title)
class Form7(Form):
    def __str__(self):
        return (self.circular_title)
class Form8(Form):
    def __str__(self):
        return (self.circular_title)
class Form9(Form):
    def __str__(self):
        return (self.circular_title)
class Form10(Form):
    def __str__(self):
        return (self.circular_title)
class teachers(models.Model):
    name=models.CharField(max_length=20, blank=True)
    middle_name=models.CharField(max_length=10, blank=True)
    surname=models.CharField(max_length=10, blank=True)
    form=models.CharField(max_length=10, blank=True)
    subject=models.CharField(max_length=100)
    contact_number=models.IntegerField()
    def __str__(self):
        return (self.name)
class every_teacher(models.Model):
    student_name=models.ForeignKey(students,on_delete=models.CASCADE)
    work_pdf=models.FileField(blank=True)