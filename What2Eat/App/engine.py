from . import models
import random


def search():
    owned_products = models.Product.objects.filter(owned=True)
    recipes = models.Recipe.objects.filter(products__in=owned_products)
    possible_recipes = []
    if not owned_products:
        return 'Air'
    else:
        for recipe in recipes:
            required_products = recipe.products.all()
            common_elements = required_products.intersection(owned_products)
            if len(common_elements) == len(required_products):
                possible_recipes.append(recipe)
        if not possible_recipes:
            return 'Air'
        else:
            return random.choice(possible_recipes)
