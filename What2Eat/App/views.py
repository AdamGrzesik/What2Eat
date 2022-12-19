from django.shortcuts import render
from . import models
from .engine import search

# Deklarujemy funkcje które odpowiadają za renderowanie stron
def index(response):
    return render(response, 'App/base.html')


def homepage(response):
    products = models.Product.objects.all()
    context = {
        'products': products,
    }

    if response.method == "POST":
        if response.POST.get("save"):
            for item in products:
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.owned = True
                else:
                    item.owned = False
                item.save()

    return render(response, 'App/home.html', context)


def recipe(response):
    name = search()
    recipe = models.Recipe.objects.get(name=name)
    products = recipe.products.all()
    context = {
        'recipe': recipe,
        'products': products,
    }
    return render(response, 'App/recipe.html', context)


def copyrights(response):
    return render(response, 'App/copyrights.html')
