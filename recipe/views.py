from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe
from django.utils import timezone
from django.db.models import F
from food.models import Profile


@login_required(login_url="/account/login")
def add(request):
    profile = get_object_or_404(Profile, person=request.user)
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
        return render(request, 'recipe/add.html', {'credibility': profile.credibility})

@login_required(login_url="/account/login")
def steps(request, recipe_id):
    profile = get_object_or_404(Profile, person=request.user)
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe/steps.html', {'recipe': recipe, 'credibility': profile.credibility})

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
    recipe = Recipe.objects.all().annotate(fieldsum=F('upvotes')-F('downvotes')).order_by('-fieldsum', '-upvotes')
    profile = get_object_or_404(Profile, person=request.user)
    return render(request, 'recipe/allRecipies.html', {'recipe': recipe, 'credibility': profile.credibility})
