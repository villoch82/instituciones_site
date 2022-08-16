from django.urls import path
from . import views

urlpatterns = [
    path('crear', views.Save, name='crear'),
    path('crear/<int:id>/', views.Save, name='modificar'),
    path('registrar_usuario', views.regitrarUsuario, name='registrarUsuario'),
    path('login', views.loginUsuario, name = 'loginUsuario')
]