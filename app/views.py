from django.shortcuts import render
from .models import Student
from django.http import HttpResponse

def home(request):
    if request.method =='POST':
        data=request.POST
        name=data['name']
        age=data['age']
        email=data['email']
        message=data['message']

        user=Student(name=name,age=age,email=email,message=message)
        user.save()
        return HttpResponse("Sucessfully submitted!!!")
    return render(request,'home.html')


