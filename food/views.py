from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Food, Location, Profile
from recipe.models import Recipe
from django.utils import timezone
from django.db.models import F
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def home(request):
    food = Food.objects.all().annotate(fieldsum=F('upvotes')-F('downvotes')).order_by('-fieldsum', '-upvotes')
    try:
        profile = get_object_or_404(Profile, person=request.user)
        print(food)
        return render(request, 'food/home.html', {'food': food, 'credibility': profile.credibility})
    except:
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
                "X-RapidAPI-Key": os.environ.get('GEO_KEY'),
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

@login_required(login_url="/account/login")
def details(request, food_id):
    foood = get_object_or_404(Food, pk=food_id)
    location = Location.objects.select_related('food').get(food_id = food_id)
    profile = get_object_or_404(Profile, person=foood.contributor)
    profile2 = get_object_or_404(Profile, person=request.user)
    return render(request, 'food/details.html', {'mapKey':os.environ.get('GEO_KEY'), 'food': foood, 'latitude': location.lat, 'longitude': location.lng, 'cred': profile.credibility, 'credibility': profile2.credibility})

@login_required(login_url="/account/login")
def upvotee(request, food_id):
    if request.method == 'POST':
        food = get_object_or_404(Food, pk=food_id)
        profile = get_object_or_404(Profile, person=food.contributor)
        profile.credibility += 1
        food.upvotes += 1
        profile.save()
        food.save()
        return redirect('/food/' + str(food.id))

@login_required(login_url="/account/login")
def downvotee(request, food_id):
    if request.method == 'POST':
        food = get_object_or_404(Food, pk=food_id)
        profile = get_object_or_404(Profile, person=food.contributor)
        profile.credibility -= 1
        food.downvotes += 1
        profile.save()
        food.save()
        return redirect('/food/' + str(food.id))

@login_required(login_url="/account/login")
def personal(request):
    profile = get_object_or_404(Profile, person=request.user)
    food = Food.objects.filter(contributor=request.user)
    recipe = Recipe.objects.filter(contributor=request.user)
    return render(request, 'food/personal.html', {'food': food, 'recipe': recipe, 'credibility': profile.credibility, 'cred': profile.credibility, 'username': request.user})
