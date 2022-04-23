from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'index.html')

def cars_index(request):
    return render(request, 'cars/cars_index.html')