from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('activity/', views.activity, name='add_activity'),
    path('companion/', views.companionview, name='companion'),
    path('details/<str:username>/', views.detailed_view, name='detailed_view')
]