from django.db import models
from django.urls import reverse

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100, default= 'N/A')
    year = models.IntegerField(default=1960)
    color = models.CharField(max_length=100, default= 'N/A')
    miles = models.IntegerField(default=0)
    description = models.TextField(max_length=250, default='N/A')

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

OILTYPES = (
    ('FS', 'Full Synthectic'),
    ('S', 'Syntethic'),
    ('C', 'Conventional'),
    ('HM', "High Mileage")
)


class Oilchange(models.Model):
    date = models.DateField()
    oiltype = models.CharField(
      max_length=2,
      choices=OILTYPES,
      default=OILTYPES[0][0]
      )

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_oiltype_display()} on {self.date}"