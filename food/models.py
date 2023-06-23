from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    contributor = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_only(self):
        return self.pub_date.strftime('%b %e %y')


class Location(models.Model):
    food = models.ForeignKey(Food, on_delete = models.CASCADE)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)

class Profile(models.Model):
    person = models.ForeignKey(User, on_delete = models.CASCADE)
    credibility = models.IntegerField(default=0)
