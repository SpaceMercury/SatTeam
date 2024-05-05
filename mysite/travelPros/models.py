from django.db import models

# Create your models here.

class Traveler(models.Model):
    name = models.CharField(max_length=100)
    departure_date = models.CharField(max_length=100)
    return_date = models.CharField(max_length=100)
    departure_city = models.CharField(max_length=100, default='Barcelona')
    arrival_city = models.CharField(max_length=100, default='Paris')
    number_of_days = models.IntegerField(default=1)

    def __str__(self):
        return self.name