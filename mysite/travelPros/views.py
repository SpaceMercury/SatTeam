from django.shortcuts import render, redirect
from .forms import ActivityForm
from .models import Traveler
from django.http import HttpResponse
from .friend_find_activity import UserComparer3
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
                form.cleaned_data['arrival_city'],
                form.cleaned_data['number_of_days']
            ]

            # Path to your database file or similar resource
            
            file_path = "/Users/polfuentes/SatTeam/mysite/data/hackupc-travelperk-dataset.csv"
            df = pd.read_csv(file_path, header= 0)
            df_simple = [row[1:] for row in df.values]

            # Call your comparison function
            comparison_result = UserComparer3(user_profile, df_simple, user_profile[5])
            print(comparison_result)

            return render(request, 'companion.html', {
                'results': comparison_result,
                'user_name': user_profile[0]  # Passing the user's name
            })
        
        else:
            return HttpResponse('Invalid data')
    return render(request, 'activity.html', context)


def activityfirst(request):
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
                form.cleaned_data['arrival_city'],
                form.cleaned_data['number_of_days']
            ]

            # Path to your database file or similar resource
            
            file_path = "/Users/polfuentes/SatTeam/mysite/data/hackupc-travelperk-dataset.csv"
            df = pd.read_csv(file_path, header= 0)
            df_simple = [row[1:] for row in df.values]

            # Call your comparison function
            comparison_result = UserComparer1(user_profile[:5], df_simple)

            return render(request, 'companion_second.html', {
                'results': comparison_result,
                'user_name': user_profile[0]  # Passing the user's name
            })
        
        else:
            return HttpResponse('Invalid data')
    return render(request, 'activity_EZ.html', context)





def companionview(request):
    users = Traveler.objects.all()  # Query all activities
    return render(request, 'companion.html', {'users': users})


def detailed_view(request, username):
    print(username)
    return render(request, 'detailed_view.html', {'user': username})