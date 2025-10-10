from django.shortcuts import render

# Create your views here.

def inicio(request):
    computador_precio = 700000
    a = (computador_precio * 0.19) + computador_precio
    a = int(a)
    contexto = {'mensaje': '¡Hola desde Django!', 'valor_a': a}
    return render(request, 'inicio.html', contexto)

def index(request):
    variable = "99"
    return render(request, 'index.html', {'variable': variable})