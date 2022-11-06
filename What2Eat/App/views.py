from django.shortcuts import render
from . import models


# Deklarujemy funkcje które odpowiadają za renderowanie stron
def index(response):
    return render(response, 'App/base.html')


def homepage(response):
    products = models.Products.objects.all()
    context = {'products': products}
    return render(response, 'App/home.html', context)


def recipe(response):
    return render(response, 'App/recipe.html')


def copyrights(response):
    return render(response, 'App/copyrights.html')
