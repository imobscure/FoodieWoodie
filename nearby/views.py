from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from food.models import Location
from .models import Nearby
from django.db.models import F
import requests
from math import cos, asin, sqrt, pi

def distance(lat1, lon1, lat2, lon2):
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a))

@login_required(login_url="/account/login")
def proximity(request):
    if request.method == 'POST':
        refLat = request.latitude
        refLng = request.longitude
        food = Location.objects.all().annotate(fieldsum=distance(refLat, refLng, F('lat'), F('lng'))).order_by('fieldsum')
        return render(request, 'nearby/proximity.html', {'food': food})
    else:
        return render(request, 'nearby/proximity.html', {'food': 0})
