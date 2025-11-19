from django.urls import path
from . import views

urlpatterns = [
    path('bicicleta/<int:pk>/', views.detalle_bicicleta_con_resenas, name='detalle_bicicleta'),
    path('bicicleta/<int:bicicleta_id>/resena/crear/', views.crear_resena, name='crear_resena'),
    path('resena/<int:pk>/editar/', views.editar_resena, name='editar_resena'),
    path('resena/<int:pk>/eliminar/', views.eliminar_resena, name='eliminar_resena'),
    path('mis-resenas/', views.mis_resenas, name='mis_resenas'),
]
