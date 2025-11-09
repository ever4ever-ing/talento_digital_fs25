from django.urls import path
from .views import (
    ListaEventos, MisEventos,
    CrearEvento, EditarEvento, EliminarEvento, AccesoDenegadoView,
    UnirseEventoView, SalirseEventoView, ParticipantesEventoView
)

urlpatterns = [
    path('', ListaEventos.as_view(), name='lista_eventos'),
    path('mis_eventos/', MisEventos.as_view(), name='mis_eventos'),
    path('crear_evento/', CrearEvento.as_view(), name='crear_evento'),
    path('editar_evento/<int:pk>/', EditarEvento.as_view(), name='editar_evento'),
    path('eliminar_evento/<int:pk>/', EliminarEvento.as_view(), name='eliminar_evento'),
    path('evento/<int:pk>/unirse/', UnirseEventoView.as_view(), name='unirse_evento'),
    path('evento/<int:pk>/salirse/', SalirseEventoView.as_view(), name='salirse_evento'),
    path('evento/<int:pk>/participantes/', ParticipantesEventoView.as_view(), name='participantes_evento'),
    path('acceso-denegado/', AccesoDenegadoView.as_view(), name='acceso_denegado'),
]