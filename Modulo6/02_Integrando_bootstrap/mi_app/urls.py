from django.urls import path
from . import views

app_name = 'mi_app'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('home/', views.home, name='home'),
    path('perfil/', views.perfil, name='perfil'),
]