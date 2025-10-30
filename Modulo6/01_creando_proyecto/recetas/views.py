from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Receta

# Create your views here.

def lista_recetas(request):
    recetas = Receta.objects.all()
    context = {'recetas': recetas}
    return render(request, 'recetas/inicio.html', context)





