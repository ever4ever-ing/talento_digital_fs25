from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Profesor, Curso, Estudiante, Perfil, Inscripcion
from .forms import ProfesorForm, CursoForm, EstudianteForm, PerfilForm, InscripcionForm

class MenuAcademicoView(TemplateView):
	template_name = 'academico/menu.html'
 
class ProfesorListView(ListView):
	model = Profesor
	template_name = 'academico/profesor_list.html'
	context_object_name = 'profesores'

class CursoListView(ListView):
	model = Curso
	template_name = 'academico/curso_list.html'
	context_object_name = 'cursos'

class EstudianteListView(ListView):
	model = Estudiante
	template_name = 'academico/estudiante_list.html'
	context_object_name = 'estudiantes'

class PerfilListView(ListView):
	model = Perfil
	template_name = 'academico/perfil_list.html'
	context_object_name = 'perfiles'

class InscripcionListView(ListView):
	model = Inscripcion
	template_name = 'academico/inscripcion_list.html'
	context_object_name = 'inscripciones'

class ProfesorCreateView(CreateView):
	model = Profesor
	form_class = ProfesorForm
	template_name = 'academico/profesor_form.html'
	success_url = reverse_lazy('profesor_create')

class CursoCreateView(CreateView):
	model = Curso
	form_class = CursoForm
	template_name = 'academico/curso_form.html'
	success_url = reverse_lazy('curso_create')

class EstudianteCreateView(CreateView):
	model = Estudiante
	form_class = EstudianteForm
	template_name = 'academico/estudiante_form.html'
	success_url = reverse_lazy('estudiante_create')

class PerfilCreateView(CreateView):
	model = Perfil
	form_class = PerfilForm
	template_name = 'academico/perfil_form.html'
	success_url = reverse_lazy('perfil_create')

class InscripcionCreateView(CreateView):
	model = Inscripcion
	form_class = InscripcionForm
	template_name = 'academico/inscripcion_form.html'
	success_url = reverse_lazy('inscripcion_create')
