from django.urls import path
from . import views

urlpatterns = [
    path('crear', views.Save, name='crear'),
    path('crear/<int:id>/', views.Save, name='modificar'),
]