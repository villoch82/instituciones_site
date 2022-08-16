from django.urls import path
from . import views

app_name = 'instituciones'

urlpatterns = [
    path('', views.Listar, name = 'listado'),
    path('crear', views.Save, name = 'crear'),
    path('crear/<int:id>/', views.Save, name = 'modificar'),
    path('registrar_usuario', views.regitrarUsuario, name = 'registrarUsuario'),
    path('login', views.loginUsuario, name = 'loginUsuario'),
    path('logout', views.logoutUsuario, name = 'logoutUsuario'),
    path('eliminar', views.Borrar, name = 'eliminar')
]