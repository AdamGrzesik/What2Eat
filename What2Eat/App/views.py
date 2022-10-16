from django.shortcuts import render
from django.http import HttpResponse


def index(response):
    return render(response, 'App/base.html', {
        'content': 'Podstawowa strona',
        'button_text': 'Dodatkowa strona',
    })


def testing_view(response):
    return render(response, 'App/view1.html', {
        'content': 'Strona dodatkowa',
        'button_text': 'Podstawowa strona',
    })
