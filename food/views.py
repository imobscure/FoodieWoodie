from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Food, Location
from django.utils import timezone
from django.db.models import F
import requests

def home(request):
    food = Food.objects.all().annotate(fieldsum=F('upvotes')-F('downvotes')).order_by('-fieldsum', '-upvotes')
    return render(request, 'food/home.html', {'food': food})

@login_required(login_url="/account/login")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['image'] and request.FILES['icon']:
            food = Food()
            food.title = request.POST['title']
            food.body = request.POST['body']
            string = request.POST['url']
            food.url = string
            food.image = request.FILES['image']
            food.icon = request.FILES['icon']
            food.pub_date = timezone.datetime.now()
            food.contributor = request.user
            food.save()
            location = Location()
            location.food = food
            url = "https://trueway-geocoding.p.rapidapi.com/Geocode"
            headers = {
                "X-RapidAPI-Key": "1dc0964288msh31f40a1f1c5f2c3p1c0e6djsnab87c2f869f6",
                "X-RapidAPI-Host": "trueway-geocoding.p.rapidapi.com"
            }
            querystring = {"address":str(string),"language":"en"}
            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()
            location.lat = data['results'][0]['location']['lat']
            location.lng = data['results'][0]['location']['lng']
            location.save()
            return redirect('/food/'+str(food.id))
        else:
            return render(request, 'food/create.html', {'error': 'All the Fields are mandatory.'})
    else:
        return render(request, 'food/create.html')

def details(request, food_id):
    foood = get_object_or_404(Food, pk=food_id)
    location = Location.objects.select_related('food').get(food_id = food_id)
    return render(request, 'food/details.html', {'food': foood, 'latitude': location.lat, 'longitude': location.lng})

@login_required(login_url="/account/login")
def upvotee(request, food_id):
    if request.method == 'POST':
        food = get_object_or_404(Food, pk=food_id)
        food.upvotes += 1
        food.save()
        return redirect('/food/' + str(food.id))

@login_required(login_url="/account/login")
def downvotee(request, food_id):
    if request.method == 'POST':
        food = get_object_or_404(Food, pk=food_id)
        food.downvotes += 1
        food.save()
        return redirect('/food/' + str(food.id))
