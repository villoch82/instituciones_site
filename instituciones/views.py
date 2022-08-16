from django import forms
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm


from instituciones.forms import CrearInstitucionForm, RegistraUsuarioForm
from instituciones.models import Instituciones

# Create your views here.
def Listar(request):
    usuario_actual = request.user
    if not request.user.is_authenticated:
        messages.info(request, 'No se permite el acceso anónimo')
        return redirect('instituciones:loginUsuario')

    listado = Instituciones.objects.all().filter(creado_por = usuario_actual)
    return render(
        request,
        'listado.html',
        context = {
            'listado' : listado,
        }
    )

def Save(request):
    id = ''
    action = 'CREAR'
    usuario_actual = request.user

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
            institucion.creado_por = usuario_actual

            institucion.save()
            messages.info(request, 'Datos almacenados correctamente')

    elif request.GET:
            
            institucion = Instituciones.objects.get(id = request.GET['id'])
            
            data = {
                'nombre' : institucion.nombre,
                'direccion' : institucion.direccion,
                'fecha_creacion' : institucion.fecha_creacion,
                'nif' : institucion.nif,
                'creado_por' : current_user.id
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

def Borrar(request):
    if request.GET:
        if 'id' and 'confirmado' in request.GET:
            try:
                Instituciones.objects.filter(id = request.GET['id']).delete()
                messages.info(request, 'Institucion eliminada')
                return redirect('instituciones:listado')
            except ValueError:
                messages.error(request, 'hubo un error al eliminar la institución')
        elif request.GET['id']:
            return render(
                request,
                'eliminar.html',
                context = {
                    'id' : request.GET['id'],
                }
            )



def regitrarUsuario(request):
    if request.method == "POST":
        form = RegistraUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Usuario registrado" )
            return redirect('instituciones:login')
        messages.error(request, "Error al registrar nuevo usuario, revise los datos suministrados")
    form = RegistraUsuarioForm()
    return render(
        request, 
        "usuario_registrar.html", 
        context={"form":form})

def loginUsuario(request):
    if request.POST:
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.info(request, 'Sesión inisciada como ' + username)
                return redirect('instituciones:listado')
            else:
                messages.error(request, 'Usuario y/o contraseña inválido')
        else:
            messages.error(request, 'Usuario y/o contraseña inválido')
    form = AuthenticationForm()
    return render(
        request,
        'login.html',
        context={
            'form' : form,
        }
    )

def logoutUsuario(request):
    logout(request)
    messages.info(request, 'Ha cerrado la sessión')
    return redirect('instituciones:loginUsuario')