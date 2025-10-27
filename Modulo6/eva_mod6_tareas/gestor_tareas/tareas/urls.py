from django.urls import path
from . import views

app_name = 'tareas'

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('detalle/<int:tarea_id>/', views.detalle_tarea, name='detalle_tarea'),
    path('agregar/', views.agregar_tarea, name='agregar_tarea'),
    path('eliminar/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
]