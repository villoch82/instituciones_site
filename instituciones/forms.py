from django import forms
from django.core.validators import RegexValidator
from instituciones.models import Instituciones

NIF_REGEX = RegexValidator("[0-9]{8}[a-zA-Z]{1}", 'No es un formato NIF válido')

class CrearInstitucionForm(forms.Form):
    nombre = forms.CharField(max_length=60)
    direccion = forms.CharField(max_length= 100)
    fecha_creacion = forms.DateTimeField()
    nif = forms.CharField(validators=[NIF_REGEX], max_length=9)

