from django.urls import path
from .views import EditarPost, ListaPosts, MisPosts

urlpatterns = [
    path('', ListaPosts.as_view(), name='lista_posts'),
    path('mis-posts/', MisPosts.as_view(), name='mis_posts'),
    path('editar/', EditarPost.as_view(), name='editar_post'),
]