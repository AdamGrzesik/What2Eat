from django.shortcuts import render
from . import models


# Deklarujemy funkcje które odpowiadają za renderowanie stron
def index(response):
    return render(response, 'App/base.html')


def homepage(response):
    products_quan = models.ProductsQuan.objects.all()
    products_nonquan = models.ProductsNonQuan.objects.all()
    context = {
        'products_quan': products_quan,
        'products_nonquan': products_nonquan,

    }
    return render(response, 'App/home.html', context)


def recipe(response, id):
    recipe = models.Recipe.objects.get(id=id)
    products_quan = models.ProductsQuan.objects.filter(recipes=id)
    products_nonquan = models.ProductsNonQuan.objects.filter(recipes=id)
    context = {
        'recipe': recipe,
        'products_quan': products_quan,
        'products_nonquan': products_nonquan,
    }
    return render(response, 'App/recipe.html', context)


def copyrights(response):
    return render(response, 'App/copyrights.html')
