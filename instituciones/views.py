from django import forms
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm


from instituciones.forms import CrearInstitucionForm, RegistraUsuarioForm
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

def regitrarUsuario(request):
    if request.method == "POST":
        form = RegistraUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Usuario registrado" )
            return redirect("main:homepage")
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