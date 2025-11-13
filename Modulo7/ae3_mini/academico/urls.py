from django.urls import path
from .views import (
    MenuAcademicoView,
    ProfesorCreateView,
    CursoCreateView,
    EstudianteCreateView,
    PerfilCreateView,
    InscripcionCreateView,
    ProfesorListView,
    CursoListView,
    EstudianteListView,
    PerfilListView,
    InscripcionListView,
)

urlpatterns = [
    path('', MenuAcademicoView.as_view(), name='menu_academico'),
    path('profesor/crear/', ProfesorCreateView.as_view(), name='profesor_create'),
    path('profesor/lista/', ProfesorListView.as_view(), name='profesor_list'),
    path('curso/crear/', CursoCreateView.as_view(), name='curso_create'),
    path('curso/lista/', CursoListView.as_view(), name='curso_list'),
    path('estudiante/crear/', EstudianteCreateView.as_view(), name='estudiante_create'),
    path('estudiante/lista/', EstudianteListView.as_view(), name='estudiante_list'),
    path('perfil/crear/', PerfilCreateView.as_view(), name='perfil_create'),
    path('perfil/lista/', PerfilListView.as_view(), name='perfil_list'),
    path('inscripcion/crear/', InscripcionCreateView.as_view(), name='inscripcion_create'),
    path('inscripcion/lista/', InscripcionListView.as_view(), name='inscripcion_list'),
]
