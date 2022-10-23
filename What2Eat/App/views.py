from django.shortcuts import render


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
