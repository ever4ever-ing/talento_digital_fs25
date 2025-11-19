from django.contrib import admin
from .models import Evento, Inscripcion


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo_evento', 'fecha_hora', 'cupo_disponible', 'cupo_maximo', 'precio', 'activo']
    list_filter = ['tipo_evento', 'dificultad', 'activo', 'fecha_hora']
    search_fields = ['nombre', 'destino', 'descripcion']
    list_editable = ['activo']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'descripcion', 'tipo_evento', 'dificultad', 'imagen')
        }),
        ('Detalles del Evento', {
            'fields': ('destino', 'punto_encuentro', 'fecha_hora', 'duracion_horas', 'distancia_km')
        }),
        ('Cupos y Precio', {
            'fields': ('cupo_maximo', 'cupo_disponible', 'precio')
        }),
        ('Inclusiones', {
            'fields': ('incluye_guia', 'incluye_seguro', 'incluye_hidratacion', 'incluye_snacks')
        }),
        ('Requisitos', {
            'fields': ('nivel_minimo',)
        }),
        ('Estado', {
            'fields': ('activo', 'created_at', 'updated_at')
        }),
    )


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'evento', 'num_personas', 'estado', 'pagado', 'total_pagado', 'fecha_inscripcion']
    list_filter = ['estado', 'pagado', 'fecha_inscripcion']
    search_fields = ['cliente__nombre', 'cliente__email', 'evento__nombre']
    list_editable = ['estado', 'pagado']
    readonly_fields = ['fecha_inscripcion', 'total_pagado']
    
    fieldsets = (
        ('Información del Evento', {
            'fields': ('evento', 'cliente', 'num_personas')
        }),
        ('Contacto de Emergencia', {
            'fields': ('contacto_emergencia', 'telefono_emergencia', 'observaciones')
        }),
        ('Estado y Pago', {
            'fields': ('estado', 'pagado', 'total_pagado', 'fecha_inscripcion')
        }),
    )
    
    actions = ['confirmar_inscripciones', 'cancelar_inscripciones']
    
    def confirmar_inscripciones(self, request, queryset):
        for inscripcion in queryset:
            if inscripcion.estado == 'pendiente':
                inscripcion.estado = 'confirmada'
                inscripcion.save()
        self.message_user(request, f'{queryset.count()} inscripciones confirmadas.')
    confirmar_inscripciones.short_description = "Confirmar inscripciones seleccionadas"
    
    def cancelar_inscripciones(self, request, queryset):
        for inscripcion in queryset:
            inscripcion.cancelar()
        self.message_user(request, f'{queryset.count()} inscripciones canceladas.')
    cancelar_inscripciones.short_description = "Cancelar inscripciones seleccionadas"
