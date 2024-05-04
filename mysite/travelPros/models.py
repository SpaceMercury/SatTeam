from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=100)
    departure_date = models.DateField()
    arrival_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.departure_date} to {self.arrival_date}"
    def getDate(self):
        return f"{self.departure_date} to {self.arrival_date}"
    