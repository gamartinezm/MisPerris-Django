from django.conf.urls import url, include
from django.urls import path 
from .views import mascota_list

urlpatterns = [
	#path('', views.mascota_list, name='mascota_list'),
	path(r'', views.index, name='index'),
	path(r'formulario', views.formulario, name='formulario'),
	path(r'servicios', views.servicios, name='servicios'),
	path(r'somos', views.somos, name='somos'),
	url(r'^listar$', mascota_list, name='mascota_list'),
	#path(r'rescatado', mascota_view, name='mascota_view'),
	#url(r'^$', index, name='index'),
]

