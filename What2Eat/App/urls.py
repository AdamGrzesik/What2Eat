from django.urls import path
from . import views

# Tutaj na podstawie url przekierowywujemy pod konkretną funkcję
urlpatterns = [
    path("", views.homepage, name='homepage'),
    path("copyrights/", views.copyrights, name='copyrights'),
    path("recipe/", views.recipe, name='recipe'),
]
