from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("agenda/mes/", views.mes, name="meses"),
    path("agenda/prueba/", views.prueba, name="prueba"),
    path("agenda/borrarevento/<int:pk>", views.borrar_evento, name="borrar"),
]