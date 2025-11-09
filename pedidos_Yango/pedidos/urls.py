from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.ProductoListView.as_view(), name='producto_list'),
    path('productos/<int:pk>/', views.ProductoDetailView.as_view(), name='producto_detail'),
    path('productos/crear/', views.ProductoCreateView.as_view(), name='producto_create'),
    path('productos/<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='producto_update'),
    path('productos/<int:pk>/eliminar/', views.ProductoDeleteView.as_view(), name='producto_delete'),
    path('direcciones/', views.DireccionListView.as_view(), name='direccion_list'),
    path('direcciones/crear/', views.DireccionCreateView.as_view(), name='direccion_create'),
    path('direcciones/<int:pk>/editar/', views.DireccionUpdateView.as_view(), name='direccion_update'),
    path('direcciones/<int:pk>/eliminar/', views.DireccionDeleteView.as_view(), name='direccion_delete'),
    path('pedidos/', views.pedido_list, name='pedido_list'),
    path('pedidos/crear/', views.pedido_create, name='pedido_create'),
    path('pedidos/<int:pk>/', views.pedido_detail, name='pedido_detail'),
    path('pedidos/<int:pk>/eliminar/', views.pedido_delete, name='pedido_delete'),
    path('register/', views.register, name='register'),
]