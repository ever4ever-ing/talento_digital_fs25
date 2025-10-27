from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.event_list, name='event_list'),
    # la ruta para registrar un evento luego llama a la vista register_event definida en views.py
    # esta vista maneja tanto la visualización del formulario como el procesamiento de los datos enviados
    # el request se pasa automáticamente a la vista
    path('register/', views.register_event, name='register_event'),
    path('<int:pk>/', views.event_detail, name='event_detail'),
]
