from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Receta

# Create your views here.

def recetas(request):
    recetas = {
        'titulo': 'Bienvenidos a la página de recetas',
        'descripcion': 'Aquí encontrarás las mejores recetas de cocina.',
        'recetas': [
            {'nombre': 'Tarta de manzana', 'ingredientes': ['manzanas', 'harina', 'azúcar', 'mantequilla']},
            {'nombre': 'Ensalada César', 'ingredientes': ['lechuga', 'pollo', 'queso parmesano', 'aderezo César']},
            {'nombre': 'Spaghetti Carbonara', 'ingredientes': ['spaghetti', 'huevos', 'queso pecorino', 'panceta']}
        ]
    }
    return render(request, 'recetas/inicio.html', recetas)



