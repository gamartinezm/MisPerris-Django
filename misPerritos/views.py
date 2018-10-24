from django.shortcuts import render
from django.utils import timezone
from .models import RescatadosPost

# Create your views here.

def rescatados_list(request):
    rescatadosPosts = RescatadosPost.objects.filter()
    return render(request, 'misPerritos/rescatados_list.html', {'rescatadosPosts' : rescatadosPosts})