from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def home(response):
    
    peoples = [
        {'name': 'Abhijeet Gupta', 'age' :26},
        {'name': 'Rohan Sharma' ,'age' : 23},
        {'name': 'Vicky Kaushal' , 'age': 17},
        {'name': 'DeepanShu chaurasiya', 'age':16},
        {'name': 'Sandeep', 'age' : 63}
    ]
    # print(peoples)
    return render(response,'home.html',context={'people':peoples})
    # return HttpResponse(peoples)