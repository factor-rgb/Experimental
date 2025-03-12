from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("agenda/crear acontecimiento/", views.AgendaCreateView.as_view(), name="agregarfecha"),
    path("agenda/mes/", views.mes, name="mes"),
]