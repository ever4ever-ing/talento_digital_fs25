from django.db import models
from app_clientes.models import Cliente
from app_bicicletas.models import Bicicleta

class Orden(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='ordenes'
    )
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('pendiente', 'Pendiente'),
            ('pagada', 'Pagada'),
            ('cancelada', 'Cancelada')
        ],
        default='pendiente'
    )
    bicicletas = models.ManyToManyField(
        Bicicleta,
        through='DetalleOrden',
        related_name='ordenes'
    )

    def calcular_total(self):
        """Calcula y actualiza el total de la orden basado en los detalles"""
        total = sum(
            detalle.cantidad * detalle.precio_unitario
            for detalle in self.detalles.all()
        )
        self.total = total
        self.save()
        return total

    def __str__(self):
        return f"Orden #{self.id} - {self.cliente.nombre}"

    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Órdenes"
        ordering = ['-fecha']


class DetalleOrden(models.Model):
    orden = models.ForeignKey(
        Orden,
        on_delete=models.CASCADE,
        related_name='detalles'
    )
    bicicleta = models.ForeignKey(
        Bicicleta,
        on_delete=models.CASCADE
    )
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        """Calcula el subtotal de este detalle"""
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"{self.cantidad} x {self.bicicleta.marca} {self.bicicleta.modelo}"

    class Meta:
        verbose_name = "Detalle de Orden"
        verbose_name_plural = "Detalles de Órdenes"