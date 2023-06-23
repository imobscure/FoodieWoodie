from django.urls import path
from . import views

urlpatterns = [
    path('proximity', views.proximity, name = "proximity"),
]
