from django import forms
from django.http import HttpResponseNotFound
from django.shortcuts import render
from instituciones.forms import CrearInstitucionForm
from instituciones.models import Instituciones

# Create your views here.
def Save(request):
    id = ''
    action = 'CREAR'

    if request.POST:
        form = CrearInstitucionForm(request.POST)

        if form.is_valid():

            if request.POST['id'] == '':
                institucion = Instituciones()
                
            else:
                institucion = Instituciones.objects.get(id = request.POST['id'])
                id = request.POST['id']
                action = 'ACTUALIZAR'

            institucion.nombre = request.POST['nombre']
            institucion.direccion = request.POST['direccion']
            institucion.fecha_creacion = request.POST['fecha_creacion']
            institucion.nif = request.POST['nif']

            institucion.save()

    elif request.GET:
            
            institucion = Instituciones.objects.get(id = request.GET['id'])
            
            data = {
                'nombre' : institucion.nombre,
                'direccion' : institucion.direccion,
                'fecha_creacion' : institucion.fecha_creacion,
                'nif' : institucion.nif
            }

            form = CrearInstitucionForm(data)
            id = request.GET['id']
            action = 'ACTUALIZAR'

    else:

        form = CrearInstitucionForm()

    return render(
        request, 
        "save.html", 
        context={
            'form': form, 
            'id' : id,
            'action' : action,
            }
        )

        



        