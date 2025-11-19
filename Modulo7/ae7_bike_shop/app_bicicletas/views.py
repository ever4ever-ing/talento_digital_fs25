from django.shortcuts import get_object_or_404, render
from .models import Bicicleta
from django.shortcuts import render, redirect
from .forms import BicicletaForm
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib import messages


def es_personal(user):
    return user.groups.filter(name='Personal').exists()


def lista_bicicletas(request):
    bicicletas = Bicicleta.objects.all()
    return render(request, 'bicicletas/lista_bicicletas.html', {'bicicletas': bicicletas})


@login_required(login_url='login')
@user_passes_test(es_personal, login_url='lista_bicicletas') # Vista protegida: solo personal puede crear bicicletas
@permission_required('app_bicicletas.add_bicicleta', raise_exception=True)
def crear_bicicleta(request):
    if request.method == 'POST':
        form = BicicletaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bicicleta creada exitosamente.')
            return redirect('lista_bicicletas')
    else:
        form = BicicletaForm()
    return render(request, 'bicicletas/crear_bicicleta.html', {'form': form})


@login_required(login_url='login')
@user_passes_test(es_personal, login_url='lista_bicicletas') # Vista protegida: solo personal puede actualizar bicicletas
@permission_required('app_bicicletas.change_bicicleta', raise_exception=True)
def actualizar_bicicleta(request, pk):
    """Vista protegida: solo personal puede actualizar bicicletas"""
    bicicleta = Bicicleta.objects.get(pk=pk)
    if request.method == 'POST':
        form = BicicletaForm(request.POST, request.FILES, instance=bicicleta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bicicleta actualizada exitosamente.')
            return redirect('lista_bicicletas')
    else:
        form = BicicletaForm(instance=bicicleta)
    return render(request, 'bicicletas/crear_bicicleta.html', {'form': form, 'actualizar': True, 'bicicleta': bicicleta})


@login_required(login_url='login')
@user_passes_test(es_personal, login_url='lista_bicicletas') # Vista protegida: solo personal puede eliminar bicicletas
@permission_required('app_bicicletas.delete_bicicleta', raise_exception=True) # Vista protegida: solo personal puede eliminar bicicletas
def eliminar_bicicleta(request, pk):
    """Vista protegida: solo personal puede eliminar bicicletas"""
    bicicleta = get_object_or_404(Bicicleta, pk=pk)
    bicicleta.delete()
    messages.success(request, 'Bicicleta eliminada exitosamente.')
    return redirect('lista_bicicletas')
