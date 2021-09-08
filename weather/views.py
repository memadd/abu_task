from django.shortcuts import render
from .forms import WeatherForm
from .models import Weather

def weather_form(request):
    form = WeatherForm(request.POST or None)
    context = {
            "form": form, 
        }
    if request.method == 'POST' and form.is_valid():
        weather = form.save(commit=False)
        weather.save()
        return render(request, 'weather/home.html', context)
    return render(request, 'weather/home.html', context)

    
def list_weather(request):
    listings = Weather.objects.all()
    return render(request,'weather/listings.html', {'listings':listings})