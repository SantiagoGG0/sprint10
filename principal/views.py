from django.shortcuts import render

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
