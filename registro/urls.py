from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("peticion/", views.get_name, name="petición")
]