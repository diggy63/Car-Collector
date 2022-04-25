from django.db import models

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100, default= 'N/A')
    year = models.IntegerField(default=1960)
    color = models.CharField(max_length=100, default= 'N/A')
    description = models.TextField(max_length=250, default='N/A')