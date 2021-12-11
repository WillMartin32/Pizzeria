from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name