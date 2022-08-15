from dataclasses import field
from django import forms
from django.contrib import admin

from instituciones.models import Instituciones

class InstitucionesAdmin(admin.ModelAdmin):
    fields = ['nombre', 'direccion', 'nif', 'fecha_creacion']
    list_display = ['nombre', 'direccion', 'nif', 'fecha_creacion']

# Register your models here.
admin.site.register(Instituciones, InstitucionesAdmin)