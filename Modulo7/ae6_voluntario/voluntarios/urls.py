"""
URL Configuration para la app voluntarios
"""
from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),
    
    # URLs de Voluntarios
    path('voluntarios/', views.lista_voluntarios, name='lista_voluntarios'),
    path('voluntarios/crear/', views.crear_voluntario, name='crear_voluntario'),
    path('voluntarios/<int:pk>/', views.detalle_voluntario, name='detalle_voluntario'),
    path('voluntarios/<int:pk>/editar/', views.editar_voluntario, name='editar_voluntario'),
    path('voluntarios/<int:pk>/eliminar/', views.eliminar_voluntario, name='eliminar_voluntario'),
    
    # URLs de Eventos
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('eventos/crear/', views.crear_evento, name='crear_evento'),
    path('eventos/<int:pk>/', views.detalle_evento, name='detalle_evento'),
    path('eventos/<int:pk>/editar/', views.editar_evento, name='editar_evento'),
    path('eventos/<int:pk>/eliminar/', views.eliminar_evento, name='eliminar_evento'),
    path('eventos/<int:evento_pk>/asignar/', views.asignar_voluntario, name='asignar_voluntario'),
]
