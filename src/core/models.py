from django.db import models

class Agenda(models.Model):
    descripcion = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField(null=True, blank=True)