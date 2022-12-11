from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    owned = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='Lorem ipsum')
    tags = models.JSONField(default=['tag1','tag2','tag3','tag4'])
    products = models.ManyToManyField(Product, related_name='products', blank=True)


    def __str__(self):
        return self.name
