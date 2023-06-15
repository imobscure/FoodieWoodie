from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Food
from django.utils import timezone

def home(request):
    food = Food.objects
    return render(request, 'food/home.html', {'food': food})

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['image'] and request.FILES['icon']:
            food = Food()
            food.title = request.POST['title']
            food.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                food.url = request.POST['url']
            else:
                food.url = 'https://' + request.POST['url']
            food.image = request.FILES['image']
            food.icon = request.FILES['icon']
            food.pub_date = timezone.datetime.now()
            food.contributor = request.user
            food.save()
            return redirect('/food/'+str(food.id))
        else:
            return render(request, 'food/create.html', {'error': 'All the Fields are mandatory.'})
    else:
        return render(request, 'food/create.html')

def details(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    return render(request, 'food/details.html', {'food': food})

@login_required
def upvote(request, food_id):
    if request.method == 'POST':
        food = get_object_or_404(Food, pk=food_id)
        food.upvotes += 1
        food.save()
        return redirect('/food/' + str(food.id))

@login_required
def downvote(request, food_id):
    if request.method == 'POST':
        food = get_object_or_404(Food, pk=food_id)
        food.downvotes += 1
        food.save()
        return redirect('/food/' + str(food.id))
