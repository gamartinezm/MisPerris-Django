from django.shortcuts import render

# Create your views here.

def rescatados_list(request):
    return render(request, 'misPerritos/rescatados_list.html', {})