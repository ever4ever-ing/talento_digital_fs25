from django.contrib import admin
from django.urls import path, include
from ventas import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
     path('', views.lista_automoviles, name='lista_automoviles'),
     path('crear/', views.crear_automovil, name='crear_automovil'),
     path('login/', LoginView.as_view(template_name='login.html'), name='login'),
     path('logout/', LogoutView.as_view(next_page='login'), name='logout'), 
]