from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_form, name='weather_form'),
    path('list', views.list_weather, name='list_weather'),
    
]