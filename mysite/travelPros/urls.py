from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('activity/', views.activity, name='add_activity'),
]