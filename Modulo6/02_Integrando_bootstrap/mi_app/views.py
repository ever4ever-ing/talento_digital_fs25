from django.shortcuts import render


def inicio(request):
     contexto = {'mensaje': '¡Hola desde Cuevana4ever!'}
     return render(request, 'inicio.html', contexto)