from django.shortcuts import render
from .models import Bicicleta
from django.shortcuts import render, redirect
from .forms import BicicletaForm


def crear_bicicleta(request):
    if request.method == 'POST':
        form = BicicletaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_bicicletas')
    else:
        form = BicicletaForm()
    return render(request, 'crear_bicicleta.html', {'form': form})


def actualizar_bicicleta(request, pk):
    bicicleta = Bicicleta.objects.get(pk=pk)
    if request.method == 'POST':
        form = BicicletaForm(request.POST, request.FILES, instance=bicicleta)
        if form.is_valid():
            form.save()
            return redirect('lista_bicicletas')
    else:
        form = BicicletaForm(instance=bicicleta)
    return render(request, 'crear_bicicleta.html', {'form': form, 'actualizar': True, 'bicicleta': bicicleta})


def lista_bicicletas(request):
    bicicletas = Bicicleta.objects.all()
    return render(request, 'lista_bicicletas.html', {'bicicletas': bicicletas})


def eliminar_bicicleta(request, pk):
    bicicleta = get_object_or_404(Bicicleta, pk=pk)
    bicicleta.delete()
    return redirect('lista_bicicletas')