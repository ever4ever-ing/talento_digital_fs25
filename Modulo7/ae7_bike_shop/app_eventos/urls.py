from django.urls import path
from . import views

urlpatterns = [
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('eventos/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
    path('eventos/<int:evento_id>/inscribirse/', views.inscribirse_evento, name='inscribirse_evento'),
    path('mis-inscripciones/', views.mis_inscripciones, name='mis_inscripciones'),
    path('inscripcion/<int:inscripcion_id>/cancelar/', views.cancelar_inscripcion, name='cancelar_inscripcion'),
]
