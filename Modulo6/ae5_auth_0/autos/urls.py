from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('autos/crear/', views.crear_auto, name='crear_auto'),
    path('autos/', views.lista_autos, name='lista_autos'),  # vista de lista de autos
    path('home/', views.home, name='home'),

]