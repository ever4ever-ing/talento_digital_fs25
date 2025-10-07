from django.urls import path
from . import views

app_name = 'mi_app'

urlpatterns = [
    path('', views.inicio, name='inicio'),
]