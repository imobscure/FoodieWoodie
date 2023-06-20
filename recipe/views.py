from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe
from django.utils import timezone


@login_required(login_url="/account/login")
def add(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.FILES['image']:
            recipe = Recipe()
            recipe.title = request.POST['title']
            recipe.body = request.POST['body']
            recipe.image = request.FILES['image']
            recipe.pub_date = timezone.datetime.now()
            recipe.contributor = request.user
            recipe.save()
            return redirect('/recipe/'+str(recipe.id))
        else:
            return render(request, 'recipe/add.html', {'error': 'All the Fields are mandatory.'})
    else:
        return render(request, 'recipe/add.html')

def steps(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe/steps.html', {'recipe': recipe})

@login_required(login_url="/account/login")
def upvote(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        recipe.upvotes += 1
        recipe.save()
        return redirect('/recipe/' + str(recipe.id))

@login_required(login_url="/account/login")
def downvote(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        recipe.downvotes += 1
        recipe.save()
        return redirect('/recipe/' + str(recipe.id))

@login_required(login_url="/account/login")
def all(request):
    recipe = Recipe.objects
    return render(request, 'recipe/allRecipies.html', {'recipe': recipe})
