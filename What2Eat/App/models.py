from django.db import models


class ProductsQuan(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ProductsNonQuan(models.Model):
    name = models.CharField(max_length=100)
    owned = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='nic')
    products = models.ManyToManyField(ProductsQuan)
    products_non = models.ManyToManyField(ProductsNonQuan)

    def __str__(self):
        return self.name
