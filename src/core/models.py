from django.db import models

class Agenda(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField(null=True, blank=True)

class Horarios(models.Model):
    asunto = models.CharField(max_length=30)
    hora = models.DateTimeField()