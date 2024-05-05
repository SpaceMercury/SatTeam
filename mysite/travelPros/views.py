from django.shortcuts import render, redirect
from .forms import ActivityForm
from .models import Traveler
from django.http import HttpResponse
from .friend_find_activity import UserComparer1
import pandas as pd
# Create your views here.

def home(request):
    return render(request, 'home.html')



def activity(request):

    form = ActivityForm()
    context = {'form': form}

    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():

            Traveler.objects.all().delete()
            form.save()

            user_profile = [
                form.cleaned_data['name'],
                form.cleaned_data['departure_date'],
                form.cleaned_data['arrival_date'],
                form.cleaned_data['departure_city'],
                form.cleaned_data['arrival_city']
            ]

            # Path to your database file or similar resource
            
            file_path = "/Users/polfuentes/SatTeam/mysite/data/hackupc-travelperk-dataset.csv"

            df = pd.read_csv(file_path, header= 0)

            df_simple = [row[1:] for row in df.values]

            # Call your comparison function
            comparison_result = UserComparer1(user_profile, df_simple)

            return render(request, 'companion.html', {'result': comparison_result})
        
        else:
            return HttpResponse('Invalid data')
    return render(request, 'activity.html', context)


def companionview(request):
    users = Traveler.objects.all()  # Query all activities
    return render(request, 'companion.html', {'users': users})
