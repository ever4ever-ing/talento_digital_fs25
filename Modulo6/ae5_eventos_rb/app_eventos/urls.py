from django.urls import path
from .views import ListaEventos, MisEventos, LoginView, LogoutView

urlpatterns = [
    path('', ListaEventos.as_view(), name='lista_eventos'),
    path('mis_eventos/', MisEventos.as_view(), name='mis_eventos'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]