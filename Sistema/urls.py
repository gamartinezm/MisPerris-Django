from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	url(r"^nosotros/$", views.nosotros, name = "nosotros"),
	url(r"^servicios/$", views.servicios, name = "servicios"),
	url(r"^contacto/$", views.contacto, name = "contacto"),
	url(r"^registro/$", views.registro, name = "registro"),
	url(r"^adopcion/$", views.adopcion_mascota, name = "adopcionMascota"),
	url(r"^adopcion/adoptar/(?P<pk>[0-9_]+)$", views.adoptar_mascota, name = "adoptarMascota"),
	url(r"^mismascotas/$", views.mascotas_adoptante, name = "mascotasAdoptante"),

	url(r"^gestion/adoptantes/$", views.gestion_adoptantes, name = "gestionAdoptantes"),
	url(r"^gestion/adoptantes/(?P<pk>[0-9_]+)$", views.ver_adoptante, name = "verAdoptante"),
	url(r"^gestion/adoptantes/actualizar/(?P<pk>[0-9_]+)$", views.actualizar_adoptante, name = "actualizarAdoptante"),
	url(r"^gestion/adoptantes/eliminar/(?P<pk>[0-9_]+)$", views.eliminar_adoptante, name = "eliminarAdoptante"),

	url(r"^gestion/mascotas/$", views.gestion_mascotas, name = "gestionMascotas"),
	url(r"^gestion/mascotas/(?P<pk>[0-9_]+)$", views.ver_mascota, name = "verMascota"),
	url(r"^gestion/mascotas/actualizar/(?P<pk>[0-9_]+)$", views.actualizar_mascota, name = "actualizarMascota"),
	url(r"^gestion/mascotas/eliminar/(?P<pk>[0-9_]+)$", views.eliminar_mascota, name = "eliminarMascota"),

	url(r"^cuentas/recuperarpass/$", views.recuperar_password, name = "recuperarPassword"),
	url(r"^cuentas/cambiarpass/(?P<token>[\w\.-]+)&(?P<user>[\w\.]+)$", views.cambiar_password, name = "cambiarPassword"),
	url(r"^cuentas/login/$", views.ingresar, name = "login"),
	url(r"^cuentas/logout/$", views.salir, name = "logout"),
	url(r"^$", views.index, name = "indice"),
]
