from django.shortcuts import render
from .models import Bicicleta

def lista_bicicletas(request):
    bicicletas = Bicicleta.objects.all()
    return render(request, 'lista_bicicletas.html', {'bicicletas': bicicletas})