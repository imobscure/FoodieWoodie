from django.db import models
from food.models import Food

class Nearby(models.Model):
    food = models.ForeignKey(Food, on_delete = models.CASCADE)
    cellid = models.IntegerField(default=0)
