from django.urls import path
from .views import RegistroView, LoginView, LogoutView, PerfilView, InfoUsuarioView

urlpatterns = [
    # Autenticación
    path('registro/', RegistroView.as_view(), name='registro'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Perfil de usuario
    path('perfil/', PerfilView.as_view(), name='perfil'),
    path('info/', InfoUsuarioView.as_view(), name='info_usuario'),
]
