# mi_tienda/urls.py
from django.contrib import admin
from django.urls import path, include # Asegúrate de importar 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('productos.urls')), # <-- Añade esta línea
]
