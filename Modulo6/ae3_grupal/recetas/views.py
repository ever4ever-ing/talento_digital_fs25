from django.shortcuts import render
from .models import Receta

# Create your views here.

def receta_list(request):

    recetas = Receta.objects.all() #Obtiene todas las recetas desde la base de datos
    
    return render(request, 'receta_list.html', {'recetas': recetas})
