from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("agenda/mes/", views.mes, name="mes"),
    path("agenda/prueba/", views.prueba, name="prueba"),
]