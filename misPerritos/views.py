from django.shortcuts import render
from django.utils import timezone
from .models import RescatadosPost

from django.http import HttpResponse

# Create your views here.

#def index(request):
#	return HttpResponse("Index")



def rescatados_list(request):
    rescatadosPosts = RescatadosPost.objects.filter()
    return render(request, 'misPerritos/rescatados_list.html', {'rescatadosPosts' : rescatadosPosts})

def index(request):    
    return render(request, 'misPerritos/index.html', {})

def formulario(request):    
    return render(request, 'misPerritos/formulario.html', {})

def somos(request):    
    return render(request, 'misPerritos/somos.html', {})

def servicios(request):    
    return render(request, 'misPerritos/servicios.html', {})
