from django.shortcuts import render
from . import models
from .engine import search
import random



# Deklarujemy funkcje które odpowiadają za renderowanie stron
def index(response):
    return render(response, 'App/base.html')


def homepage(response):
    products_quan = models.ProductsQuan.objects.all()
    products_nonquan = models.ProductsNonQuan.objects.all()

    if response.method == "POST":
        if response.POST.get("save"):
            for item in products_quan:
                if response.POST.get("q" + str(item.id)):
                    item.quantity = int(response.POST.get("q" + str(item.id)))
                    item.save()
        if response.POST.get("save"):
            for item in products_nonquan:
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.owned = True
                else:
                    item.owned = False
                item.save()
    found = search()
    context = {
        'products_quan': products_quan,
        'products_nonquan': products_nonquan,
        'found': found,
    }
    return render(response, 'App/home.html', context)


def recipe(response):
    id = search()
    recipe = models.Recipe.objects.get(id=id)
    products_quan = recipe.products.all()
    products_nonquan = recipe.products_non.all()
    products_quan_req = models.Requirement.objects.filter(recipe_id=id).values_list('requirement', flat=True)

    context = {
        'recipe': recipe,
        'products_quan': products_quan,
        'products_nonquan': products_nonquan,
        'req': products_quan_req,
    }
    return render(response, 'App/recipe.html', context)


def copyrights(response):
    return render(response, 'App/copyrights.html')
