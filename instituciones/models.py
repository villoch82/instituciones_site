from django.db import models
from django.core.validators import RegexValidator

#Regex 

# Create your models here.

class Instituciones(models.Model):

    nombre = models.CharField(max_length=60,  verbose_name='Nombre')
    direccion = models.CharField(max_length= 100, verbose_name='Dirección')
    fecha_creacion = models.DateTimeField()
    nif = models.CharField(max_length=9, verbose_name='NIF')