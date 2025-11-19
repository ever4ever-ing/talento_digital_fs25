from django.db import models
from app_clientes.models import Cliente
from django.core.exceptions import ValidationError
from django.utils import timezone


class Evento(models.Model):
    TIPO_EVENTO_CHOICES = [
        ('parque', 'Salida a Parque'),
        ('volcan', 'Salida a Volcán'),
        ('ruta_costera', 'Ruta Costera'),
        ('montana', 'Mountain Bike'),
        ('urbano', 'Tour Urbano'),
    ]
    
    DIFICULTAD_CHOICES = [
        ('facil', 'Fácil'),
        ('intermedio', 'Intermedio'),
        ('dificil', 'Difícil'),
        ('experto', 'Experto'),
    ]
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo_evento = models.CharField(max_length=20, choices=TIPO_EVENTO_CHOICES)
    dificultad = models.CharField(max_length=15, choices=DIFICULTAD_CHOICES)
    
    # Detalles del evento
    destino = models.CharField(max_length=200, help_text="Lugar de destino")
    punto_encuentro = models.CharField(max_length=200)
    fecha_hora = models.DateTimeField()
    duracion_horas = models.DecimalField(max_digits=4, decimal_places=1, help_text="Duración en horas")
    distancia_km = models.DecimalField(max_digits=5, decimal_places=1, help_text="Distancia en kilómetros")
    
    # Cupos
    cupo_maximo = models.PositiveIntegerField(default=20)
    cupo_disponible = models.PositiveIntegerField(default=20)
    
    # Costo
    precio = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio por persona")
    
    # Inclusiones
    incluye_guia = models.BooleanField(default=True)
    incluye_seguro = models.BooleanField(default=True)
    incluye_hidratacion = models.BooleanField(default=True)
    incluye_snacks = models.BooleanField(default=False)
    
    # Requisitos
    nivel_minimo = models.CharField(
        max_length=100,
        blank=True,
        help_text="Requisitos mínimos para participar"
    )
    
    # Estado
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='eventos/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['fecha_hora']
    
    def __str__(self):
        return f"{self.nombre} - {self.fecha_hora.strftime('%d/%m/%Y')}"
    
    def tiene_cupos_disponibles(self):
        """Verifica si hay cupos disponibles"""
        return self.cupo_disponible > 0
    
    def evento_pasado(self):
        """Verifica si el evento ya pasó"""
        return self.fecha_hora < timezone.now()
    
    def puede_inscribirse(self):
        """Verifica si se puede inscribir al evento"""
        return self.activo and self.tiene_cupos_disponibles() and not self.evento_pasado()
    
    def porcentaje_ocupacion(self):
        """Calcula el porcentaje de ocupación"""
        if self.cupo_maximo == 0:
            return 0
        ocupados = self.cupo_maximo - self.cupo_disponible
        return int((ocupados / self.cupo_maximo) * 100)


class Inscripcion(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('completada', 'Completada'),
    ]
    
    evento = models.ForeignKey(
        Evento,
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='inscripciones_eventos'
    )
    
    # Datos de la inscripción
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    num_personas = models.PositiveIntegerField(default=1, help_text="Número de personas")
    
    # Información adicional
    contacto_emergencia = models.CharField(max_length=100, blank=True)
    telefono_emergencia = models.CharField(max_length=20, blank=True)
    observaciones = models.TextField(blank=True, help_text="Alergias, condiciones médicas, etc.")
    
    # Estado y pago
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    pagado = models.BooleanField(default=False)
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"
        ordering = ['-fecha_inscripcion']
        unique_together = ['evento', 'cliente']  # Un cliente solo puede inscribirse una vez por evento
    
    def __str__(self):
        return f"{self.cliente.nombre} - {self.evento.nombre}"
    
    def clean(self):
        """Validaciones personalizadas"""
        if self.evento.cupo_disponible < self.num_personas:
            raise ValidationError(f'No hay suficientes cupos. Solo quedan {self.evento.cupo_disponible} cupos disponibles.')
        
        if self.evento.evento_pasado():
            raise ValidationError('No se puede inscribir a un evento que ya pasó.')
    
    def save(self, *args, **kwargs):
        # Calcular total al guardar
        if not self.total_pagado:
            self.total_pagado = self.evento.precio * self.num_personas
        
        # Si es nueva inscripción, reducir cupos
        if not self.pk and self.estado == 'confirmada':
            self.evento.cupo_disponible -= self.num_personas
            self.evento.save()
        
        super().save(*args, **kwargs)
    
    def cancelar(self):
        """Cancela la inscripción y libera cupos"""
        if self.estado != 'cancelada':
            self.estado = 'cancelada'
            self.evento.cupo_disponible += self.num_personas
            self.evento.save()
            self.save()
