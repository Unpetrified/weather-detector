from django.shortcuts import render, redirect
import json
import urllib.request
import requests
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        city = city.strip()
        if request.POST['city'] == '':
            return redirect('/')
        resp = urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=f38e390615decb03b3c16488bb2fb578&units=metric').read()
        jdata = json.loads(resp)
        data = {
        "city" : city.upper(),
        "country_code": str(jdata['sys']['country']),
        "coordinates": f"Latitude: {str(jdata['coord']['lat'])} Longitude: {str(jdata['coord']['lon'])}",
        "temp": str(jdata['main']['temp']),
        "pressure": str(jdata['main']['pressure']),
        "humidity": str(jdata['main']['humidity'])+"%",
        }
    else:
       data = {}
    return render(request, 'index.html', data)
