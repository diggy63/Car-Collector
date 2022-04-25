from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.cars_index, name="index"),
    path('cars/new', views.cars_new, name='new_car'),
    path('cars/<car_id>', views.cars_detail, name="detail"),
]