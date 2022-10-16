from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("view/", views.testing_view, name='testing_view'),
]
