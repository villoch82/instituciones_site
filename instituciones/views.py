from msilib.schema import InstallUISequence
from django.shortcuts import render
from instituciones.forms import CrearInstitucionForm
from instituciones.models import Instituciones

# Create your views here.
def Crear(request):
    

    if request.POST:
        form = CrearInstitucionForm(request.POST)

        if form.is_valid():
            institucion = Instituciones()

            institucion.nombre = request.POST['nombre']
            institucion.direccion = request.POST['direccion']
            institucion.fecha_creacion = request.POST['fecha_creacion']
            institucion.nif = request.POST['nif']

            institucion.save()

            form.nombre = institucion.nombre
            form.direccion = institucion.direccion
            form.fecha_creacion = institucion.fecha_creacion
            form.nif = institucion.nif
    else:
        form = CrearInstitucionForm()

    return render(
        request, 
        "crear.html", 
        context={"form": form}
        )

        



        