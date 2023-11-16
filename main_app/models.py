from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    def __str__(self):
        return f'{self.year} {self.make} {self.model}'