from django.urls import path
from . import views


urlpatterns = [
    path("", views.homepage, name='homepage'),
    path("recipe/", views.recipe, name='recipe'),
    path("copyrights/", views.copyrights, name='copyrights'),
]
