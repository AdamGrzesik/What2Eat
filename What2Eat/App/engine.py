from . import models
import random

def search():
    owned_products = models.Product.objects.filter(owned=True)
    print(owned_products)
    recipes = models.Recipe.objects.filter(products__in=owned_products)
    print(recipes)
    possible_recipes = []
    if not owned_products:
        return 'Air'
    else:
        for recipe in recipes:
            required_products = recipe.products.all()
            print(required_products)
            common_elements = required_products.intersection(owned_products)
            print(common_elements)
            if len(common_elements) == len(required_products):
                possible_recipes.append(recipe)
            if not possible_recipes:
                return 'Air'
        return random.choice(possible_recipes)
