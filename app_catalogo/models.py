from django.db import models

# Create your models here.

class Libro(models.Model):
    ESTADO_CHOICES = [
        ('DISPONIBLE', 'Disponible'),
        ('PRESTADO', 'Prestado'),
        ('MANTENIMIENTO', 'En mantenimiento'),
    ]
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    disponible = models.BooleanField(default=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='DISPONIBLE')
    fecha_publicacion = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo
