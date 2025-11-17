from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_bicicletas, name='lista_bicicletas'),
    path('crear/', views.crear_bicicleta, name='crear_bicicleta'),
]
