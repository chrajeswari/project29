from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
from app.forms import *

def create_student(request):
    ESFO=Studentform()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=Studentform(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('create student form')
        else:
            return HttpResponse('invalid data')
    return render(request,'create_student.html',d)