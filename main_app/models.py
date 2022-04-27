from django.db import models
from django.urls import reverse

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('services_detail', kwargs={'pk': self.pk})


class Car(models.Model):
    make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100, default= 'N/A')
    year = models.IntegerField(default=1960)
    color = models.CharField(max_length=100, default= 'N/A')
    miles = models.IntegerField(default=0)
    description = models.TextField(max_length=250, default='N/A')
    lastOilChange = models.IntegerField(default=0)
    services = models.ManyToManyField(Service)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

    def miles_until_oil(self):
        return  (6000 + self.lastOilChange) - self.miles

OILTYPES = (
    ('FS', 'Full Synthectic'),
    ('S', 'Syntethic'),
    ('C', 'Conventional'),
    ('HM', "High Mileage")
)


class Oilchange(models.Model):
    date = models.DateField()
    miles = models.IntegerField(default=0)
    oiltype = models.CharField(
      max_length=2,
      choices=OILTYPES,
      default=OILTYPES[0][0]
      )

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_oiltype_display()} on {self.date}"