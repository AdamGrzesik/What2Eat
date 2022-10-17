from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=100)
    owned = models.BooleanField()

    def __str__(self):
        return self.name
