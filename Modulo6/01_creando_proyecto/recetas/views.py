from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Receta

# Create your views here.

def lista_recetas(request):
    recetas = Receta.objects.all()
    context = {'recetas': recetas}

    return render(request, 'recetas/inicio.html', context)



