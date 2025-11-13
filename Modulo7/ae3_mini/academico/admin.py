from django.contrib import admin
from .models import Profesor, Curso, Estudiante, Perfil, Inscripcion

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'especialidad')
	search_fields = ('nombre', 'especialidad')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'profesor')
	search_fields = ('nombre',)
	list_filter = ('profesor',)

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'email')
	search_fields = ('nombre', 'email')

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
	list_display = ('id', 'estudiante', 'biografia', 'redes_sociales')
	search_fields = ('estudiante__nombre', 'redes_sociales')

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
	list_display = ('id', 'estudiante', 'curso', 'fecha_inscripcion', 'estado', 'nota_final')
	list_filter = ('estado', 'curso')
	search_fields = ('estudiante__nombre', 'curso__nombre')
