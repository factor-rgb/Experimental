from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("agenda/mes/", views.mes, name="meses"),
    path("agenda/borrar/asunto/<int:pk>", views.borrar_asunto, name="borrar_asunto"),
    path("agenda/crear/evento/", views.AgendaCreateView.as_view(), name="crear_evento"),
    path("agenda/revisar/evento/<int:pk>", views.AgendaUpdateView.as_view(), name="revisar_evento"),
    path("agenda/eliminar/evento/<int:pk>", views.AgendaDeleteView.as_view(), name="borrar_evento"),
]