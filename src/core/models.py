from django.db import models

class Agenda(models.Model):
    descripcion = models.CharField(max_length=255)
    fecha = models.DateField()