from django import forms
from .models import Region, Ciudad

PET_STATUS = (
	("Rescatado", "Rescatado"),
	("Disponible", "Disponible")
)

HOME_TYPE = (
	("Casa con patio grande", "Casa con patio grande"),
	("Casa con patio pequeño", "Casa con patio pequeño"),
	("Casa sin patio", "Casa sin patio"),
	("Departamento", "Departamento")
)

class FormAdoptante(forms.Form):
	run = forms.CharField(label = "RUN", max_length = 10, widget = forms.TextInput(attrs = { "id": "run", "class": "campo", "placeholder": "12345678-9" }))
	nombres = forms.CharField(label = "Nombres", max_length = 20, widget = forms.TextInput(attrs = { "id": "nombres", "class": "campo", "placeholder": "Ingrese nombres" }))
	apPaterno = forms.CharField(label = "Apellido paterno", max_length = 20, widget = forms.TextInput(attrs = { "id": "appaterno", "class": "campo", "placeholder" : "Ingrese apellido paterno" }))
	apMaterno = forms.CharField(label = "Apellido materno", max_length = 20, widget = forms.TextInput(attrs = { "id": "apmaterno", "class": "campo", "placeholder" : "Ingrese apellido materno" }))
	fechaNacimiento = forms.DateField(label = "Fecha de nacimiento", widget = forms.DateInput(attrs = { "id": "fecnac", "class": "campo", "placeholder": "dd/mm/yyyy" }))
	correo = forms.EmailField(label = "Correo electrónico", max_length = 30, widget = forms.EmailInput(attrs = { "id": "correo", "class": "campo", "placeholder": "direccioncorreo@correo.com" }))
	telefono = forms.IntegerField(label = "Teléfono", required = False, widget = forms.TextInput(attrs = { "id": "telefono", "class": "campo", "placeholder": "Ingrese número de teléfono" }))
	region = forms.ModelChoiceField(label = "Región", queryset = Region.objects.all(), empty_label = None, widget = forms.Select(attrs = { "id": "region", "class": "campo combobox" }))
	ciudad = forms.ModelChoiceField(label = "Ciudad", queryset = Ciudad.objects.all(), empty_label = None, widget = forms.Select(attrs = { "id": "ciudad", "class": "campo combobox" }))
	tipoVivienda = forms.ChoiceField(label = "Tipo de vivienda", choices = HOME_TYPE, widget = forms.Select(attrs = { "id": "tipo_vivienda", "class": "campo combobox" }))

class FormMascota(forms.Form):
	nombre = forms.CharField(label = "Nombre mascota", max_length = 20, widget = forms.TextInput(attrs = { "id": "nombre", "class": "campo", "placeholder": "Ingrese nombre de mascota" }))
	raza = forms.CharField(label = "Raza dominante", max_length = 20, widget = forms.TextInput(attrs = { "id": "raza", "class": "campo", "placeholder": "Ingrese raza dominante" }))
	descripcion = forms.CharField(label = "Descripción", widget = forms.Textarea(attrs = { "id": "descripcion", "class": "campo", "placeholder": "Ingrese descripción" }))
	estado = forms.ChoiceField(label = "Estado", choices = PET_STATUS, widget = forms.Select(attrs = { "id": "estado", "class": "campo combobox" }))
	foto = forms.ImageField(label = "Foto", required = False, widget = forms.ClearableFileInput(attrs = { "id": "foto" }))

class FormContacto(forms.Form):
	nombre = forms.CharField(label = "Nombre", max_length = 30, widget = forms.TextInput(attrs = { "id": "nombre", "class": "campo", "placeholder": "Ingrese nombre" }))
	correo = forms.EmailField(label = "Correo electrónico", max_length = 30, widget = forms.EmailInput(attrs = { "id": "correo", "class": "campo", "placeholder": "Ingrese correo" }))
	mensaje = forms.CharField(label = "Mensaje", widget = forms.Textarea(attrs = { "id": "mensaje", "class": "campo", "placeholder": "Ingrese mensaje de contacto" }))

class Login(forms.Form):
	username = forms.CharField(label = "Nombre de usuario", widget = forms.TextInput(attrs = { "id": "username", "class": "campo", "placeholder": "Ingrese nombre de usuario" }))
	password = forms.CharField(label = "Contraseña", widget = forms.PasswordInput(attrs = { "id": "password", "class": "campo", "placeholder": "Ingrese contraseña" }))

class FormRecuperarPassword(forms.Form):
	correo = forms.EmailField(label = "Correo electrónico", max_length = 30, widget = forms.EmailInput(attrs = { "id": "correo", "class": "campo", "placeholder": "Ingrese correo" }))

class FormCambioPassword(forms.Form):
	nuevaPassword = forms.CharField(label = "Nueva contraseña", widget = forms.PasswordInput(attrs = { "id": "nuevapass", "class": "campo", "placeholder": "Ingrese nueva contraseña" }))
	confirmPassword = forms.CharField(label = "Confirmar contraseña", widget = forms.PasswordInput(attrs = { "id": "confirmpass", "class": "campo", "placeholder": "Confirme nueva contraseña" }))
