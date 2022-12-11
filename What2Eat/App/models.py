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
    products = models.ManyToManyField(ProductsQuan, blank=True)
    products_non = models.ManyToManyField(ProductsNonQuan, blank=True)

    def __str__(self):
        return self.name


class Requirement(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(ProductsQuan, on_delete=models.DO_NOTHING)
    requirement = models.IntegerField(default=0)
    name = "Requirement"
    def __str__(self):
        return self.name