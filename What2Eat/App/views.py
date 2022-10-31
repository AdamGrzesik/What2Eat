from django.shortcuts import render

# Deklarujemy funkcje które odpowiadają za renderowanie stron
def index(response):
    return render(response, 'App/base.html', {
    })


def homepage(response):
    return render(response, 'App/home.html', {
        'content': 'Strona dodatkowa',
        'button_text': 'Podstawowa strona',
    })


def recipe(response):
    return render(response, 'App/recipe.html', {
    })


def copyrights(response):
    return render(response, 'App/copyrights.html', {
    })
