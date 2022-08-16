from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

#Regex 
NIF_REGEX = RegexValidator("[0-9]{8}[a-zA-Z]{1}", 'No es un formato NIF válido')

# Create your models here.

class Instituciones(models.Model):

    nombre = models.CharField(max_length=60,  verbose_name='Nombre')
    direccion = models.CharField(max_length= 100, verbose_name='Dirección')
    fecha_creacion = models.DateTimeField()
    nif = models.CharField(validators=[NIF_REGEX], max_length=9, verbose_name='NIF')
    creado_por = models.ForeignKey(User, on_delete= models.CASCADE, related_name='instituciones_usuario', verbose_name='Creador')


    def __str__(self):
        return self.nombre