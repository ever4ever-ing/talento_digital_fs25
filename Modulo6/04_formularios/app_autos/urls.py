from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_automoviles, name='lista_automoviles'),
    path('crear/', views.crear_automovil, name='crear_automovil'),
]