from django.shortcuts import render


def inicio(request):
     contexto = {'mensaje': '¡Hola desde Cuevana4ever!'}
     return render(request, 'inicio.html', contexto)

def home(request):
    return render(request, 'home.html')


def perfil(request):
    usuario = {"nombre": "Everardo", "edad": 28}
    return render(request, 'perfil.html', usuario)


