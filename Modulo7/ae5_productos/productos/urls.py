from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    # Define aquí las rutas de la aplicación productos
    path('', views.lista_productos, name='lista_productos'),
]
