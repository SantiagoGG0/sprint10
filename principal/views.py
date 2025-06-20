from django.shortcuts import render, redirect
from .models import Mascota, Propietario
from .forms import MascotaForm, PropietarioForm

def inicio(request):
    return render(request, 'principal/inicio.html')

def servicios(request):
    return render(request, 'principal/servicios.html')

def dinamico(request):
    contexto = {
        'mensaje': "Aquí irá contenido dinámico en el futuro.",
        'placeholder_items': ['Mascotas', 'Citas', 'Dueños']
    }
    return render(request, 'principal/dinamico.html', contexto)

def lista_mascotas(request):
    mascotas = Mascota.objects.select_related('propietario').all()
    return render(request, 'principal/mascotas.html', {'mascotas': mascotas})

def lista_propietarios(request):
    propietarios = Propietario.objects.all()
    return render(request, 'principal/lista_propietarios.html', {'propietarios': propietarios})

def registrar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mascotas')
    else:
        form = MascotaForm()
    return render(request, 'principal/registrar_mascota.html', {'form': form})

def registrar_propietario(request):
    if request.method == 'POST':
        form = PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('principal/lista_propietarios')
    else:
        form = PropietarioForm()
    return render(request, 'principal/registrar_propietario.html', {'form': form})
