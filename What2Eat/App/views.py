from django.shortcuts import render
from django.http import HttpResponse


def index(response):
    return HttpResponse('Hello there!')


def testing_view(response):
    return HttpResponse('<h1> that a view alright! </h1>')
