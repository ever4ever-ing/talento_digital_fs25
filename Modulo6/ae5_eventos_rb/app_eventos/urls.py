from django.urls import path
from .views import ListaEventos, MisEventos, LoginView, LogoutView, CrearEvento, EditarEvento, EliminarEvento 

urlpatterns = [
    path('', ListaEventos.as_view(), name='lista_eventos'),
    path('mis_eventos/', MisEventos.as_view(), name='mis_eventos'),
    path('crear_evento/', CrearEvento.as_view(), name='crear_evento'),
    path('editar_evento/<int:pk>/', EditarEvento.as_view(), name='editar_evento'),
    path('eliminar_evento/<int:pk>/', EliminarEvento.as_view(), name='eliminar_evento'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]