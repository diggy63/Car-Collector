from dataclasses import field
from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

class CarCreate(CreateView):
    model = Car
    fields = '__all__'

class CarUpdate(UpdateView):
    model = Car
    fields = '__all__'

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'



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