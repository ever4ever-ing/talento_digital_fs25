from django.urls import path
from . import views

app_name = 'recetas'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('recetas/', views.lista_recetas, name='lista_recetas'),
    path('recetas/<int:pk>/', views.detalle_receta, name='detalle_receta'),
    path('contacto/', views.contacto, name='contacto'),
    path('contacto/confirmacion/', views.confirmacion_contacto, name='confirmacion_contacto'),
]
