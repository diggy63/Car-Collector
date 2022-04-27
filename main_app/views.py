from dataclasses import field
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Car, Service
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import OilchangeForm
from django.views.generic import ListView, DetailView
# Create your views here.

class CarCreate(CreateView):
    model = Car
    fields = ['make', 'car_model', 'year', 'color', 'description', 'miles', 'lastOilChange' ]

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
    services_not_have = Service.objects.exclude(id__in = car.services.all().values_list('id'))
    oil_form = OilchangeForm()
    return render(request, 'cars/detail.html', {
        'car' : car, 
        'oil_form': oil_form,
        'services': services_not_have
    })

def add_oilchange(request, car_id):
    print(request.POST['miles'])
    car = Car.objects.get(id=car_id)
    car.miles = request.POST['miles']
    car.lastOilChange = request.POST['miles']
    car.save()
    form = OilchangeForm(request.POST)
    if form.is_valid():
        new_oilchange = form.save(commit=False)
        new_oilchange.car_id = car_id
        new_oilchange.save()
    return redirect('detail', car_id=car_id)


def cars_new(request):
    return render(request, 'cars/new.html')

def assoc_service(request, car_id, service_id):
  # Note that you can pass a toy's id instead of the whole object
  Car.objects.get(id=car_id).services.add(service_id)
  return redirect('detail', car_id=car_id)

def deassoc_service(request, car_id, service_id):
  # Note that you can pass a toy's id instead of the whole object
  Car.objects.get(id=car_id).services.remove(service_id)
  return redirect('detail', car_id=car_id)

class ServiceList(ListView):
    model = Service

class ServiceCreate(CreateView):
    model = Service
    fields = '__all__'

class ServiceDetail(DetailView):
    model = Service

class ServiceUpdate(UpdateView):
    model = Service
    fields = '__all__'

class ServiceDelete(DeleteView):
    model = Service
    success_url = '/services/'