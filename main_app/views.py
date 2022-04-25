from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
# Create your views here.

def home(request):
    return render(request, 'index.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/cars_index.html', {'cars': cars})

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/detail.html', {'car' : car})

def cars_new(request):
    return render(request, 'cars/new.html')