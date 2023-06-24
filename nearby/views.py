from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from food.models import Location, Profile
from .models import Nearby
from django.db.models import F, Value
from django.db.models.functions import Cast
import requests
from math import cos, asin, sqrt, pi
from collections import OrderedDict

def distance(lat1, lon1, lat2, lon2):
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a))

@login_required(login_url="/account/login")
def proximity(request):
    profile = get_object_or_404(Profile, person=request.user)
    if request.method == 'POST':
        addr = request.POST['address_']
        url = "https://trueway-geocoding.p.rapidapi.com/Geocode"
        headers = {
            "X-RapidAPI-Key": "1dc0964288msh31f40a1f1c5f2c3p1c0e6djsnab87c2f869f6",
            "X-RapidAPI-Host": "trueway-geocoding.p.rapidapi.com"
        }
        querystring = {"address":str(addr),"language":"en"}
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        refLat = data['results'][0]['location']['lat']
        refLng = data['results'][0]['location']['lng']
        food = {}
        for location in Location.objects.all():
            dis = distance(float(location.lat), float(location.lng), refLat, refLng)
            if dis <= 25:
                food[dis] = location.food
        food1 = OrderedDict(sorted(food.items()))
        return render(request, 'nearby/proximity.html', {'food': food1, 'credibility': profile.credibility})
    else:
        return render(request, 'nearby/proximity.html', {'food': 0, 'credibility': profile.credibility})
