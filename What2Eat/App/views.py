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
    return render(response, 'App/home.html', context)


def recipe(response, id):
    recipe = models.Recipe.objects.get(id=id)
    products_quan = recipe.products.all()
    products_nonquan = recipe.products_non.all()
    context = {
        'recipe': recipe,
        'products_quan': products_quan,
        'products_nonquan': products_nonquan,
    }
    return render(response, 'App/recipe.html', context)


def copyrights(response):
    return render(response, 'App/copyrights.html')
