from django.db import models

# Create your models here.

class Plan(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    orden = models.PositiveSmallIntegerField(default=1)
    precio = models.DecimalField(max_digits=6, decimal_places=0)
    caracteristicas = models.TextField()

    class Meta:
        ordering = ['orden']
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'

    @property
    def precio_formateado(self):
        return f"${format(self.precio, ',.0f').replace(',', '.')}"

    def __str__(self):
        return self.nombre

class Socio(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    class Meta:
        ordering = ['apellido', 'nombre']
        verbose_name = 'Socio'
        verbose_name_plural = 'Socios'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"