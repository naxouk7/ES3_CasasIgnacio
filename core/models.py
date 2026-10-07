from django.db import models
from django.utils import timezone

class Registro(models.Model):

    ESTADO_CHOICES = [
        ("aceptado", "Aceptado"),
        ("rechazado", "Rechazado"),
        ("invalido" , "Invalido")
    ]

    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    cupos = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    motivo = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=timezone.now)

    eliminado = models.BooleanField(default=False)
    fecha_eliminacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return f"{self.nombre} - {self.estado}"

    def soft_delete(self):
        self.eliminado = True
        self.fecha_eliminacion = timezone.now()
        self.save()