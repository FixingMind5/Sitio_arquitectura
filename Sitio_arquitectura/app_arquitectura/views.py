from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # Edificios: name, contexto historico y su url
    # Espacio urbano: name, ubicacion como string, autor, url
    return render(request, 'index.html')

# contact
def contact(request):
    return render(request, 'contacto.html')

# cursos
def courses(request):
    return render(request, 'cursos.html')

# nosotros
def about_us(request):
    return render(request, 'nosotros.html')