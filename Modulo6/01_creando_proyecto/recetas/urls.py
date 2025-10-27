from django.urls import path
from django.utils.module_loading import import_string
from recetas import views

app_name = 'recetas'

urlpatterns = [
    path('', views.lista_recetas, name='mis_recetas'),
]
