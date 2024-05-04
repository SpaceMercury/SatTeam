from django.shortcuts import render, redirect
from .forms import ActivityForm
from .models import Traveler
from django.http import HttpResponse

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
            print(Traveler.objects.all())
            return redirect('companion')
        else:
            return HttpResponse('Invalid data')
    return render(request, 'activity.html', context)


def companionview(request):
    users = Traveler.objects.all()  # Query all activities
    return render(request, 'companion.html', {'users': users})
