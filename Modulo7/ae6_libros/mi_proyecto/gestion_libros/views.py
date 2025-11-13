
from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'gestion_libros/crear_libro.html', {'form': form})

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'gestion_libros/lista_libros.html', {'libros': libros})

def actualizar_libro(request, pk):
    libro = Libro.objects.get(pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'gestion_libros/actualizar_libro.html', {'form': form})

def eliminar_libro(request, pk):
    libro = Libro.objects.get(pk=pk)
    libro.delete()
    return redirect('lista_libros')
