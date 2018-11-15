from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path(r'formulario', views.formulario, name='formulario'),
	path(r'servicios', views.servicios, name='servicios'),
	path(r'somos', views.somos, name='somos'),
	#url(r'^$', index),

]

