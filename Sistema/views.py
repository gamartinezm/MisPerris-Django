from django.shortcuts import render, redirect, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import Adoptante, Mascota, Mensaje
from .forms import FormContacto, FormAdoptante, FormMascota, FormRecuperarPassword, FormCambioPassword, Login
import numpy

# Create your views here.
'''
Vistas bases del sitio web
'''
def index(request):
	mascotas_chunked = None
	mascotas = Mascota.objects.all()
	# El algoritmo que sigue permite que la lista de objetos se reparta en 3 instancias
	# para poder rellenar la galería
	if len(mascotas) > 0:
		mascotas_chunked = []
		j = 0
		while j < len(mascotas):
			mascotas_chunked.append(mascotas[j:j + 3])
			j += 3
	return render(request, "index.html", { "titulo": "Inicio", "mascotas": mascotas_chunked })

def nosotros(request):
	return render(request, "nosotros.html", { "titulo": "Nosotros" })

def servicios(request):
	return render(request, "servicios.html", { "titulo": "Servicios" })

def contacto(request):
	if request.method == "POST":
		form = FormContacto(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			Mensaje.objects.create(nombre = data.get("nombre"), correo = data.get("correo"), mensaje = data.get("mensaje"))
			return redirect("contacto")
	else:
		form = FormContacto()
	return render(request, "contacto.html", { "titulo": "Contacto", "form": form })

# vista de registro de adoptantes
def registro(request):
	# en caso de que si un usuario logeado intente ingresar esta vista se redirija al indice
	if request.user.is_authenticated:
		return redirect("indice")

	if request.method == "POST":
		form = FormAdoptante(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			user = User.objects.create_user(username = (data.get("nombres")[:2] + "." + data.get("apPaterno")).lower(), password = data.get("run"), first_name = data.get("nombres").split(" ")[0], last_name = data.get("apPaterno"), email = data.get("correo"))
			Adoptante.objects.create(usuario = user, run = data.get("run"), nombres = data.get("nombres"), apPaterno = data.get("apPaterno"), apMaterno = data.get("apMaterno"), fechaNacimiento = data.get("fechaNacimiento"), telefono = data.get("telefono"), ciudad = data.get("ciudad"), tipoVivienda = data.get("tipoVivienda"))
			# despues de crear el usuario se manda un correo con las credenciales
			send_mail(
				"Registro de usuario Mis Perris",
				"Estimado nuevo usuario,\n\nGracias por unirse a nuestra platafotma, en este presente correo se encuentra sus credenciales para ingresar al sistema.\n\nNombre de usuario: %s\nContraseña: %s" % (user.username, data.get("run")),
				"donotreplymisperris@gmail.com",
				[ user.email ],
				fail_silently = True
			)
			return render(request, "signupExito.html", { "titulo": "Registro exitoso" })
	else:
		form = FormAdoptante()
	return render(request, "signup.html", { "titulo": "Registro de usuario", "form": form })

# login
def ingresar(request):
	if request.user.is_authenticated:
		return redirect("indice")

	fail = False
	if request.method == "POST":
		form = Login(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			user = authenticate(username = data.get("username"), password = data.get("password"))
			if user:
				login(request, user)
				return redirect("indice")
			fail = True
	else:
		form = Login()
	return render(request, "login.html", { "titulo": "Iniciar sesión", "form": form, "fail": fail })

# logout
def salir(request):
	if request.user.is_authenticated:
		logout(request)
	return redirect("indice")

'''
Vistas de recuperación y cambio de contraseñas
'''
def recuperar_password(request):
	fail = False
	if request.method == "POST":
		form = FormRecuperarPassword(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			try:
				user = User.objects.get(email = data.get("correo"))
			except ObjectDoesNotExist:
				user = None
			if user:
				# se generan tokens para autenticar solicitudes de recuperación de contraseñas
				token_generator = PasswordResetTokenGenerator()
				token = token_generator.make_token(user)
				# se envía un correo con el enlace para cambiar de contraseña
				send_mail(
					"Recuperación de contraseña para su cuenta de Mis Perris",
					"Estimado usuario,\n\nUsted ha solicitado recuperar la contraseña de su cuenta de Mis Perris. Para cambiar la contraseña diríjase al siguiente link: %s://%s/%s&%s" % (request.scheme, request.get_host() + "/cuentas/cambiarpass", token, user.username),
					"donotreplymisperris@gmail.com",
					[ user.email ],
					fail_silently = True
				)
				return render(request, "recuperarPasswordExito.html", { "titulo": "Solicitud de recuperación de contraseña recibida" })
			fail = True
	else:
		form = FormRecuperarPassword()
	return render(request, "recuperarPassword.html", { "titulo": "Recuperar contraseña", "form": form, "fail": fail })

def cambiar_password(request, token, user):
	contexto = { "titulo": "Cambio de contraseña" }
	try:
		usuario = User.objects.get(username = user)
	except ObjectDoesNotExist:
		usuario = None
	if usuario:
		# se verifican si los tokens que se pasan en la url son auténticos
		token_generator = PasswordResetTokenGenerator()
		if token_generator.check_token(usuario, token):
			if request.method == "POST":
				form = FormCambioPassword(request.POST)
				if form.is_valid():
					data = form.cleaned_data
					# verifica si las contraseñas son iguales
					if data.get("nuevaPassword") == data.get("confirmPassword"):
						usuario.set_password(data.get("nuevaPassword"))
						usuario.save()
						return render(request, "cambiarPasswordHecho.html", { "titulo": "Cambio de contraseña exitoso" })
			else:
				form = FormCambioPassword()
			contexto = { **contexto, **{ "user": True, "form": form } }
		else:
			contexto = { **contexto, **{ "user": True } }
	return render(request, "cambiarPassword.html", contexto)

'''
Vistas para el usuario adoptante
'''
@login_required
def adopcion_mascota(request):
	mascotas = Mascota.objects.filter(estado = "Disponible")
	paginator = Paginator(mascotas, 5) # paginador que permite repartir la lista entre 5 objetos

	try:
		pag = int(request.GET.get("page", "1"))
	except ValueError:
		pag = 1

	try:
		mascotas = paginator.page(pag)
	except (InvalidPage, EmptyPage):
		mascotas = paginator.page(paginator.num_pages)

	return render(request, "adoptarMascota.html", { "titulo": "Adoptar mascota", "mascotas": mascotas })

@login_required
def mascotas_adoptante(request):
	mascotas = Mascota.objects.filter(estado = "Adoptado", adoptante = Adoptante.objects.get(usuario = request.user))
	paginator = Paginator(mascotas, 5)

	try:
		pag = int(request.GET.get("page", "1"))
	except ValueError:
		pag = 1

	try:
		mascotas = paginator.page(pag)
	except (InvalidPage, EmptyPage):
		mascotas = paginator.page(paginator.num_pages)

	return render(request, "mascotasAdoptante.html", { "titulo": "Mis mascotas", "mascotas": mascotas })

@login_required
def adoptar_mascota(request, pk):
	try:
		mascota = Mascota.objects.get(codigoMascota = pk)
	except ObjectDoesNotExist:
		mascota = None
	if mascota:
		mascota.adoptante = Adoptante.objects.get(usuario = request.user)
		mascota.estado = "Adoptado"
		mascota.save()
		return redirect("adopcionMascota")
	return render(request, "adoptarMascotaError.html", { "titulo": "Error al adoptar mascota" })

'''
Vistas de gestión para adoptantes/mascotas
'''
@login_required
@staff_member_required
def gestion_adoptantes(request):
	if request.method == "POST":
		form = FormAdoptante(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			user = User.objects.create_user(username = (data.get("nombres")[:2] + "." + data.get("apPaterno")).lower(), password = data.get("run"), first_name = data.get("nombres").split(" ")[0], last_name = data.get("apPaterno"), email = data.get("correo"))
			Adoptante.objects.create(usuario = user, run = data.get("run"), nombres = data.get("nombres"), apPaterno = data.get("apPaterno"), apMaterno = data.get("apMaterno"), fechaNacimiento = data.get("fechaNacimiento"), telefono = data.get("telefono"), ciudad = data.get("ciudad"), tipoVivienda = data.get("tipoVivienda"))
			return redirect("gestionAdoptantes")
	else:
		form = FormAdoptante()

	adops = Adoptante.objects.all()
	paginator = Paginator(adops, 5)

	try:
		pag = int(request.GET.get("page", "1"))
	except ValueError:
		pag = 1

	try:
		adops = paginator.page(pag)
	except (InvalidPage, EmptyPage):
		adops = paginator.page(paginator.num_pages)

	return render(request, "gestionAdoptantes.html", { "titulo": "Gestión de adoptantes", "adoptantes": adops, "form": form })

@login_required
@staff_member_required
def gestion_mascotas(request):
	if request.method == "POST":
		form = FormMascota(request.POST, request.FILES)
		if form.is_valid():
			data = form.cleaned_data
			Mascota.objects.create(nombre = data.get("nombre"), raza = data.get("raza"), descripcion = data.get("descripcion"), estado = data.get("estado"), foto = request.FILES["foto"])
			return redirect("gestionMascotas")
	else:
		form = FormMascota()

	mascotas = Mascota.objects.filter(estado__in = [ "Disponible", "Rescatado" ])
	paginator = Paginator(mascotas, 5)

	try:
		pag = int(request.GET.get("page", 1))
	except ValueError:
		pag = 1

	try:
		mascotas = paginator.page(pag)
	except (InvalidPage, EmptyPage):
		mascotas = paginator.page(paginator.num_pages)

	return render(request, "gestionMascotas.html", { "titulo": "Gestión de mascotas", "mascotas": mascotas, "form": form })

'''
Vistas para ver objetos
'''
@login_required
@staff_member_required
def ver_adoptante(request, pk):
	try:
		adoptante = Adoptante.objects.get(codigoAdoptante = pk)
	except ObjectDoesNotExist:
		adoptante = None
	return render(request, "verAdoptante.html", { "titulo": "Viendo adoptante %s" % adoptante.run, "adoptante": adoptante })

@login_required
@staff_member_required
def ver_mascota(request, pk):
	try:
		mascota = Mascota.objects.get(codigoMascota = pk)
	except ObjectDoesNotExist:
		mascota = None
	return render(request, "verMascota.html", { "titulo": "Viendo mascota %s" % mascota.nombre, "mascota": mascota })

'''
Vistas para eliminar objetos
'''
@login_required
@staff_member_required
def eliminar_adoptante(request, pk):
	try:
		adop = Adoptante.objects.get(codigoAdoptante = pk)
	except ObjectDoesNotExist:
		adop = None
	if adop:
		user = adop.usuario
		adop.delete()
		user.delete()
		return redirect("gestionAdoptantes")
	return render(request, "eliminarAdoptanteError.html", { "titulo": "Error al eliminar adoptante" })

@login_required
@staff_member_required
def eliminar_mascota(request, pk):
	try:
		mascota = Mascota.objects.get(codigoMascota = pk)
	except ObjectDoesNotExist:
		mascota = None
	if mascota:
		mascota.delete()
		return redirect("gestionMascotas")
	return render(request, "eliminarMascotaError.html", { "titulo": "Error al eliminar mascota" })

'''
Vistas para actualizar objetos
'''
@login_required
@staff_member_required
def actualizar_adoptante(request, pk):
	try:
		adop = Adoptante.objects.get(codigoAdoptante = pk)
	except ObjectDoesNotExist:
		adop = None
	if not adop:
		return render(request, "editarAdoptante.html", { "titulo": "Adoptante no existente", "form": None })

	if request.method == "POST":
		form = FormAdoptante(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			user = adop.usuario
			user.username = (data.get("nombres")[:2] + "." + data.get("apPaterno")).lower()
			user.email = data.get("correo")
			user.save()
			adop.run = data.get("run")
			adop.nombres = data.get("nombres")
			adop.apPaterno = data.get("apPaterno")
			adop.apMaterno = data.get("apMaterno")
			adop.fechaNacimiento = data.get("fechaNacimiento")
			adop.telefono = data.get("telefono")
			adop.ciudad = data.get("ciudad")
			adop.tipoVivienda = data.get("tipoVivienda")
			adop.save()
			return redirect("gestionAdoptantes")
	else:
		form = FormAdoptante({ "run": adop.run, "nombres": adop.nombres, "apPaterno": adop.apPaterno, "apMaterno": adop.apMaterno, "fechaNacimiento": adop.fechaNacimiento, "correo": adop.usuario.email, "telefono": adop.telefono, "region": adop.ciudad.region.codigoRegion, "ciudad": adop.ciudad.codigoCiudad, "tipoVivienda": adop.tipoVivienda })
	return render(request, "editarAdoptante.html", { "titulo": "Editando adoptante %s" % adop.run, "form": form })

@login_required
@staff_member_required
def actualizar_mascota(request, pk):
	try:
		mascota = Mascota.objects.get(codigoMascota = pk)
	except ObjectDoesNotExist:
		mascota = None
	if not mascota:
		return render(request, "editarMascota.html", { "titulo": "Mascota no existente", "form": None })

	if request.method == "POST":
		form = FormMascota(request.POST, request.FILES)
		if form.is_valid():
			data = form.cleaned_data
			mascota.nombre = data.get("nombre")
			mascota.raza = data.get("raza")
			mascota.descripcion = data.get("descripcion")
			if request.FILES.get("foto"):
				mascota.foto = request.FILES["foto"]
			mascota.save()
			return redirect("gestionMascotas")
	else:
		form = FormMascota({ "nombre": mascota.nombre, "raza": mascota.raza, "descripcion": mascota.descripcion, "estado": mascota.estado, "foto": mascota.foto })
	return render(request, "editarMascota.html", { "titulo": "Editando mascota %s" % mascota.nombre, "form": form })
