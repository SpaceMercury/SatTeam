from django.forms import ModelForm
from .models import Traveler


class ActivityForm(ModelForm):
    class Meta:
        model = Traveler
        fields = ['name', 'departure_date', 'arrival_date', 'departure_city', 'arrival_city', 'number_of_days']
