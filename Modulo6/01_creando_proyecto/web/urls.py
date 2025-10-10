from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('index', views.index, name='index'),
]