from django.shortcuts import render

# Create your views here.
#Agregada la funcion inicio
def inicio(request):
     contexto = {'mensaje': '¡Hola desde Django!'}
     return render(request, 'mi_aplicacion/inicio.html', contexto)








# def recibir_dato(request, valor):
#     contexto = {'valor': valor}
#     return render(request, 'mi_aplicacion/inicio.html', contexto)

