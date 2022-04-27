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
    path('cars/<int:car_id>/add_oilchange/', views.add_oilchange, name='add_oilchange'),
    path('services/', views.ServiceList.as_view(), name='services_index'),
    path('services/create/', views.ServiceCreate.as_view(), name='services_create'),
    path('services/<int:pk>/', views.ServiceDetail.as_view(), name='services_detail'),
    path('services/<int:pk>/update/', views.ServiceUpdate.as_view(), name='services_update'),
    path('services/<int:pk>/delete/', views.ServiceDelete.as_view(), name='services_delete'),
    path('cats/<int:car_id>/assoc_service/<int:service_id>/', views.assoc_service, name='assoc_service'),
    path('cats/<int:car_id>/deassoc_service/<int:service_id>/', views.deassoc_service, name='deassoc_service'),
]