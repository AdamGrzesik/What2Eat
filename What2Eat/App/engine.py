from . import models
import random

def search():
    found_recipes = models.Recipe.objects.all()
    owned_products_q = models.ProductsQuan.objects.filter(quantity__gt=0).values_list('id', flat=True)
    owned_products_nq = models.ProductsNonQuan.objects.filter(owned=True)
    print(owned_products_q)

    if len(owned_products_q) != 0:
        first_filter = found_recipes.filter(products__id=owned_products_q[0])
        for item in owned_products_q[1:]:
            first_filter = first_filter.filter(products__id=item)
        print(first_filter)
        for item in first_filter:
            req = models.Requirement.objects.filter(recipe_id=item.id)
            for product in owned_products_q:
                one = req.filter(product_id=product).values_list('requirement', flat=True)
                two = models.ProductsQuan.objects.filter(id=product).values_list('quantity', flat=True)
                if one.first() is None:
                    pass
                elif one.first() <= two.first():
                    second_filter = first_filter
                else:
                    second_filter = first_filter.exclude(id=item.id)
                    break
    else:
        second_filter = found_recipes

    if len(owned_products_nq) != 0:

        third_filter = second_filter.filter(products_non__name=owned_products_nq[0])
        for item in found_recipes[1:]:
            third_filter = third_filter.filter(products_non__name=item)
    else:
        third_filter = second_filter

    if (len(owned_products_q) == 0) and (len(owned_products_nq) == 0):
        third_filter = found_recipes.none()

    if third_filter.first() is None:
        third_filter = found_recipes.none()
        found_id = 11
    else:
        third_filter = random.choice(third_filter)
        found_id = models.Recipe.objects.filter(name=third_filter).values_list('id', flat=True)
        found_id = found_id[0]
    print(found_id)
    return found_id