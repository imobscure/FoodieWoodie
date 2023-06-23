from django.urls import path
from . import views

urlpatterns = [
    path('personal', views.personal, name = "personal"),
    path('create', views.create, name = "create"),
    path('<int:food_id>', views.details, name = "details"),
    path('<int:food_id>/upvotee', views.upvotee, name = "upvotee"),
    path('<int:food_id>/downvotee', views.downvotee, name = "downvotee"),
]
