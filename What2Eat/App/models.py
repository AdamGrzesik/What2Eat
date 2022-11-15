from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='nic')

    def __str__(self):
        return self.name


class ProductsQuan(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.name


class ProductsNonQuan(models.Model):
    name = models.CharField(max_length=100)
    owned = models.BooleanField(default=False)
    recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.name
