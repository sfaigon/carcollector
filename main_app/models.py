from django.db import models
from django.urls import reverse
from datetime import date

OILS = (
    ('R', 'Regular'),
    ('H', 'Hybrid'),
    ('S', 'Synthetic')
)

class Accessory(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('accessories_detail', kwargs={'pk': self.id})

class Car(models.Model):
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    accessories = models.ManyToManyField(Accessory)
    def __str__(self):
        return f'{self.year} {self.make} {self.model}'
    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})
class OilChange(models.Model):
    date = models.DateField('Oil Change Date')
    oil = models.CharField(
        max_length=1,
        choices=OILS,
        default=OILS[0][0]
    )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.get_oil_display()} on {self.date}'
    class Meta:
        ordering = ['-date']