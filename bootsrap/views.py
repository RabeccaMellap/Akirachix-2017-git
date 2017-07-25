from django.shortcuts import render
from django.http import HttpResponse
from.models import Student

# Create your views here.

def welcome(request):
    return  render(request,"index.html")

def students(request):
    students = Student.objects.all()
    return HttpResponse(students)
    
    


