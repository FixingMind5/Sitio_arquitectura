from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserRegistrationForm

# Create your views here.
def index(request):
    # Edificios: name, contexto historico y su url
    # Espacio urbano: name, ubicacion como string, autor, url
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'usuario {username} registrado!')
            return redirect('index')
    else:
        form = UserRegistrationForm()

    context = { 'form': form }

    return render(request, 'register.html', context)

# contact
def contact(request):
    return render(request, 'contacto.html')

# cursos
def courses(request):
    return render(request, 'cursos.html')

# nosotros
def about_us(request):
    return render(request, 'nosotros.html')