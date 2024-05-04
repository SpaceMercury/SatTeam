from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'departure_date', 'arrival_date']
