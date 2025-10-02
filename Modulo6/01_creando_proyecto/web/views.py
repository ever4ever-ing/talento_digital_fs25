from django.shortcuts import render

# Create your views here.

def inicio(request):
    a = 10 + 1
    contexto = {'mensaje': '¡Hola desde Django!', 'valor_a': a}
    return render(request, 'web/inicio.html', contexto)