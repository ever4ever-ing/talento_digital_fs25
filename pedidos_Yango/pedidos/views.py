from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Producto, Pedido, PedidoProducto, Direccion

# Create your views here.

class ProductoListView(ListView):
    model = Producto
    template_name = 'pedidos/producto_list.html'
    context_object_name = 'productos'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'pedidos/producto_detail.html'

class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'pedidos/producto_form.html'
    fields = ['nombre', 'descripcion', 'precio', 'stock']
    success_url = reverse_lazy('producto_list')

class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = 'pedidos/producto_form.html'
    fields = ['nombre', 'descripcion', 'precio', 'stock']
    success_url = reverse_lazy('producto_list')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'pedidos/producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')

class DireccionListView(ListView):
    model = Direccion
    template_name = 'pedidos/direccion_list.html'
    context_object_name = 'direcciones'

    def get_queryset(self):
        return Direccion.objects.filter(usuario=self.request.user)

class DireccionCreateView(CreateView):
    model = Direccion
    template_name = 'pedidos/direccion_form.html'
    fields = ['calle', 'numero', 'ciudad', 'codigo_postal', 'pais']
    success_url = reverse_lazy('direccion_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class DireccionUpdateView(UpdateView):
    model = Direccion
    template_name = 'pedidos/direccion_form.html'
    fields = ['calle', 'numero', 'ciudad', 'codigo_postal', 'pais']
    success_url = reverse_lazy('direccion_list')

    def get_queryset(self):
        return Direccion.objects.filter(usuario=self.request.user)

class DireccionDeleteView(DeleteView):
    model = Direccion
    template_name = 'pedidos/direccion_confirm_delete.html'
    success_url = reverse_lazy('direccion_list')

    def get_queryset(self):
        return Direccion.objects.filter(usuario=self.request.user)

@login_required
def pedido_list(request):
    pedidos = Pedido.objects.filter(usuario=request.user)
    return render(request, 'pedidos/pedido_list.html', {'pedidos': pedidos})

@login_required
def pedido_create(request):
    if request.method == 'POST':
        # Obtener productos, cantidades y dirección
        productos_ids = request.POST.getlist('productos')
        cantidades = request.POST.getlist('cantidades')
        direccion_id = request.POST.get('direccion')
        
        if productos_ids and cantidades and direccion_id:
            try:
                direccion = Direccion.objects.get(id=direccion_id, usuario=request.user)
                pedido = Pedido.objects.create(usuario=request.user, direccion=direccion, total=0)
                total = 0
                for prod_id, cant in zip(productos_ids, cantidades):
                    try:
                        producto = Producto.objects.get(id=prod_id)
                        cantidad = int(cant)
                        if cantidad > 0 and producto.stock >= cantidad:
                            PedidoProducto.objects.create(pedido=pedido, producto=producto, cantidad=cantidad)
                            total += producto.precio * cantidad
                            producto.stock -= cantidad
                            producto.save()
                    except (Producto.DoesNotExist, ValueError):
                        pass
                pedido.total = total
                pedido.save()
                return redirect('pedido_list')
            except Direccion.DoesNotExist:
                pass
    productos = Producto.objects.all()
    direcciones = Direccion.objects.filter(usuario=request.user)
    return render(request, 'pedidos/pedido_form.html', {'productos': productos, 'direcciones': direcciones})

@login_required
def pedido_detail(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk, usuario=request.user)
    return render(request, 'pedidos/pedido_detail.html', {'pedido': pedido})

@login_required
def pedido_delete(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk, usuario=request.user)
    if request.method == 'POST':
        # Restaurar stock
        for pp in pedido.pedidoproducto_set.all():
            pp.producto.stock += pp.cantidad
            pp.producto.save()
        pedido.delete()
        return redirect('pedido_list')
    return render(request, 'pedidos/pedido_confirm_delete.html', {'pedido': pedido})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def home(request):
    return render(request, 'pedidos/home.html')
