from django.urls import path
from . import views

urlpatterns = [
    path('', views.receta_list, name='receta_list'),
]