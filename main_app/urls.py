from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.cars_index, name="index"),
    path('cars/new', views.cars_new, name='new_car'),
    path('cars/<car_id>', views.cars_detail, name='detail'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete', views.CarDelete.as_view(), name='cars_delete'),
    path('cars/<int:car_id>/add_oilchange/', views.add_oilchange, name='add_oilchange')
]