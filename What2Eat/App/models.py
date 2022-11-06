from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='DUPA')

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=100)
    owned = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)
    recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.name
