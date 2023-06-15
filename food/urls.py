from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name = "create"),
    path('<int:food_id>', views.details, name = "details"),
    path('<int:food_id>/upvote', views.upvote, name = "upvote"),
    path('<int:food_id>/downvote', views.downvote, name = "downvote"),
]
