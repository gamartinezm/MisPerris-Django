from django.shortcuts import render
from .models import Mascota
from .models import Estado


# Create your views here.

def index(request):    
    return render(request, 'misPerritos/index.html', {})


def formulario(request):    
    return render(request, 'misPerritos/formulario.html', {})


def somos(request):    
    return render(request, 'misPerritos/somos.html', {})


def servicios(request):    
    return render(request, 'misPerritos/servicios.html', {})

def mascota_list(request):
	mascota = Mascota.objects.all()
	contexto = {'mascotas': mascotas}
    return render(request, 'misPerritos/mascota_list.html', contexto)
