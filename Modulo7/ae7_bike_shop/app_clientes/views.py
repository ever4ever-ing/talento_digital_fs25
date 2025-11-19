from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User, Group
from django.db.models import Count, Sum, Avg, Q
from .forms import ClienteRegistroForm, ClienteLoginForm, PerfilClienteForm
from .models import Cliente, PerfilCliente


# Función auxiliar para verificar si el usuario es personal
def es_personal(user):
    """Verifica si el usuario pertenece al grupo 'Personal'"""
    return user.groups.filter(name='Personal').exists()


# Función auxiliar para verificar si el usuario es cliente
def es_cliente(user):
    """Verifica si el usuario pertenece al grupo 'Cliente'"""
    return user.groups.filter(name='Cliente').exists()


@require_http_methods(["GET", "POST"])
def registro(request):
    """
    Vista para registrar nuevos usuarios (clientes)
    """
    if request.user.is_authenticated:
        return redirect('lista_bicicletas')

    if request.method == 'POST':
        form = ClienteRegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Agregar al grupo 'Cliente'
            cliente_group, created = Group.objects.get_or_create(name='Cliente')
            user.groups.add(cliente_group)
            
            # Crear perfil del cliente
            PerfilCliente.objects.get_or_create(
                cliente=Cliente.objects.get(email=user.email)
            )
            
            messages.success(request, '¡Registro exitoso! Por favor, inicia sesión.')
            return redirect('login')
    else:
        form = ClienteRegistroForm()

    return render(request, 'clientes/registro.html', {'form': form})


@require_http_methods(["GET", "POST"])
def login_view(request):
    """
    Vista para iniciar sesión
    """
    if request.user.is_authenticated:
        return redirect('lista_bicicletas')

    if request.method == 'POST':
        form = ClienteLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido, {user.first_name}!')
                return redirect('lista_bicicletas')
    else:
        form = ClienteLoginForm()

    return render(request, 'clientes/login.html', {'form': form})


@login_required(login_url='login')
def logout_view(request):
    """
    Vista para cerrar sesión
    """
    logout(request)
    messages.success(request, 'Sesión cerrada correctamente.')
    return redirect('lista_bicicletas')


@login_required(login_url='login')
def perfil(request):
    """
    Vista para mostrar y editar el perfil del usuario
    """
    cliente = Cliente.objects.get(email=request.user.email)
    perfil, created = PerfilCliente.objects.get_or_create(cliente=cliente)

    if request.method == 'POST':
        form = PerfilClienteForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('perfil')
    else:
        form = PerfilClienteForm(instance=perfil)

    return render(request, 'clientes/perfil.html', {
        'form': form,
        'usuario': request.user,
        'cliente': cliente
    })


@login_required(login_url='login')
@user_passes_test(es_personal, login_url='lista_bicicletas')
@permission_required('app_bicicletas.add_bicicleta', raise_exception=True)
def crear_bicicleta_protegida(request):
    """
    Vista protegida: solo personal puede crear bicicletas
    """
    from app_bicicletas.forms import BicicletaForm
    from django.shortcuts import render, redirect

    if request.method == 'POST':
        form = BicicletaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bicicleta creada exitosamente.')
            return redirect('lista_bicicletas')
    else:
        form = BicicletaForm()

    return render(request, 'crear_bicicleta.html', {'form': form})


@login_required(login_url='login')
@user_passes_test(es_personal, login_url='lista_bicicletas')
@permission_required('app_bicicletas.change_bicicleta', raise_exception=True)
def actualizar_bicicleta_protegida(request, pk):
    """
    Vista protegida: solo personal puede actualizar bicicletas
    """
    from app_bicicletas.models import Bicicleta
    from app_bicicletas.forms import BicicletaForm

    bicicleta = Bicicleta.objects.get(pk=pk)
    if request.method == 'POST':
        form = BicicletaForm(request.POST, request.FILES, instance=bicicleta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bicicleta actualizada exitosamente.')
            return redirect('lista_bicicletas')
    else:
        form = BicicletaForm(instance=bicicleta)

    return render(request, 'crear_bicicleta.html', {
        'form': form,
        'actualizar': True,
        'bicicleta': bicicleta
    })


@login_required(login_url='login')
@user_passes_test(es_personal, login_url='lista_bicicletas')
@permission_required('app_bicicletas.delete_bicicleta', raise_exception=True)
def eliminar_bicicleta_protegida(request, pk):
    """
    Vista protegida: solo personal puede eliminar bicicletas
    """
    from app_bicicletas.models import Bicicleta

    bicicleta = Bicicleta.objects.get(pk=pk)
    bicicleta.delete()
    messages.success(request, 'Bicicleta eliminada exitosamente.')
    return redirect('lista_bicicletas')


@login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff, login_url='lista_bicicletas')
def panel_clientes(request):
    """
    Vista de administración: muestra listado de clientes y estadísticas
    Solo accesible para usuarios staff/admin
    """
    from app_ordenes.models import Orden
    from app_resenas.models import Resena
    from app_eventos.models import Inscripcion
    
    # Obtener todos los clientes con anotaciones
    clientes = Cliente.objects.select_related('perfil').order_by('-created_at')
    
    # Agregar estadísticas manualmente para cada cliente
    clientes_con_stats = []
    for cliente in clientes:
        # Buscar el usuario asociado por email
        try:
            user = User.objects.get(email=cliente.email)
            total_resenas = Resena.objects.filter(usuario=user).count()
        except User.DoesNotExist:
            total_resenas = 0
        
        # Obtener estadísticas
        ordenes = Orden.objects.filter(cliente=cliente)
        total_ordenes = ordenes.count()
        total_gastado_dict = ordenes.filter(estado='pagado').aggregate(total=Sum('total'))
        total_gastado = total_gastado_dict['total'] if total_gastado_dict['total'] else 0
        total_inscripciones = Inscripcion.objects.filter(cliente=cliente).count()
        
        # Agregar atributos al cliente
        cliente.total_ordenes = total_ordenes
        cliente.total_gastado = total_gastado
        cliente.total_resenas = total_resenas
        cliente.total_inscripciones = total_inscripciones
        clientes_con_stats.append(cliente)
    
    # Estadísticas generales
    total_clientes = len(clientes_con_stats)
    clientes_con_ordenes = len([c for c in clientes_con_stats if c.total_ordenes > 0])
    clientes_con_resenas = len([c for c in clientes_con_stats if c.total_resenas > 0])
    clientes_con_inscripciones = len([c for c in clientes_con_stats if c.total_inscripciones > 0])
    
    # Total de ingresos
    total_ingresos = Orden.objects.filter(estado='pagado').aggregate(
        total=Sum('total')
    )['total'] or 0
    
    # Promedio de gasto por cliente
    clientes_con_gasto = [c for c in clientes_con_stats if c.total_gastado > 0]
    promedio_gasto = sum(c.total_gastado for c in clientes_con_gasto) / len(clientes_con_gasto) if clientes_con_gasto else 0
    
    # Top 5 clientes por gasto
    top_clientes = sorted([c for c in clientes_con_stats if c.total_gastado > 0], 
                         key=lambda x: x.total_gastado, reverse=True)[:5]
    
    # Clientes recientes (últimos 10)
    clientes_recientes = clientes_con_stats[:10]
    
    contexto = {
        'clientes': clientes_con_stats,
        'clientes_recientes': clientes_recientes,
        'total_clientes': total_clientes,
        'clientes_con_ordenes': clientes_con_ordenes,
        'clientes_con_resenas': clientes_con_resenas,
        'clientes_con_inscripciones': clientes_con_inscripciones,
        'total_ingresos': total_ingresos,
        'promedio_gasto': promedio_gasto,
        'top_clientes': top_clientes,
    }
    
    return render(request, 'clientes/panel_clientes.html', contexto)

