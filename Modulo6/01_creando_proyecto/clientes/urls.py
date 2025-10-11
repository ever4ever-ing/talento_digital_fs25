from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.lista_productos, name='lista_productos'),
]