from django.shortcuts import render, redirect
from .forms import BookingForm
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

