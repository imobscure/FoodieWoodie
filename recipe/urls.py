from django.urls import path
from . import views

urlpatterns = [
    path('all', views.all, name = "all"),
    path('add', views.add, name = "add"),
    path('<int:recipe_id>', views.steps, name = "steps"),
    path('<int:recipe_id>/upvote', views.upvote, name = "upvote"),
    path('<int:recipe_id>/downvote', views.downvote, name = "downvote"),
]
