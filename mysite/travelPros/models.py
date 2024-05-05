from django.db import models

# Create your models here.

class Traveler(models.Model):
    name = models.CharField(max_length=100)
    departure_date = models.CharField(max_length=100)
    arrival_date = models.CharField(max_length=100)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)

    def __str__(self):
        return self.name