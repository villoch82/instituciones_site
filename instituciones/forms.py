from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#crear instituciones
NIF_REGEX = RegexValidator("[0-9]{8}[a-zA-Z]{1}", 'No es un formato NIF válido')

class CrearInstitucionForm(forms.Form):
    nombre = forms.CharField(max_length=60)
    direccion = forms.CharField(max_length= 100)
    fecha_creacion = forms.DateTimeField()
    nif = forms.CharField(validators=[NIF_REGEX], max_length=9)

#Registrar nuevo usuario
class RegistraUsuarioForm(UserCreationForm):
	email = forms.EmailField(required = True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit = True):
		user = super(RegistraUsuarioForm, self).save(commit = False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

